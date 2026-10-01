import fs from 'fs';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const WORKSPACE_ROOT = path.resolve(__dirname, '../../../../');

// Locate brave-mcp dynamically
const candidateMcpDirs = [
  path.resolve(WORKSPACE_ROOT, 'brave-mcp'),
  path.resolve(WORKSPACE_ROOT, '../Browser activity/brave-mcp')
];
const BRAVE_MCP_DIR = candidateMcpDirs.find(d => fs.existsSync(d)) || candidateMcpDirs[0];

const browserModuleUrl = pathToFileURL(path.join(BRAVE_MCP_DIR, 'src', 'browser.js')).href;
const telemetryModuleUrl = pathToFileURL(path.join(BRAVE_MCP_DIR, 'src', 'telemetry.js')).href;

const { BraveManager } = await import(browserModuleUrl);
const { telemetry } = await import(telemetryModuleUrl);

export const ENROLLED_SUBJECTS = [
  { name: 'Computer Graphics Programming', classId: '5713354' },
  { name: 'Euthenics 2', classId: '5713244' },
  { name: 'Game Development', classId: '5712641' },
  { name: 'Information Assurance and Security', classId: '5713238' },
  { name: 'IT Capstone Project 2', classId: '5713247' },
  { name: 'IT Service Management', classId: '5713245' },
  { name: 'Network Technology 2', classId: '5713246' }
];

async function downloadSubjectHandouts(page, subject) {
  const courseFolder = subject.name.replace(/\s+/g, '_');
  const subjectDir = path.join(WORKSPACE_ROOT, 'courses', courseFolder, 'handouts');
  const syllabiDir = path.join(WORKSPACE_ROOT, 'courses', courseFolder, 'syllabi');
  if (!fs.existsSync(subjectDir)) {
    fs.mkdirSync(subjectDir, { recursive: true });
  }

  telemetry.log(`Navigating to ${subject.name} (Class ID: ${subject.classId})`, 'info');
  console.log(`\n📚 [${subject.name}] (Class ID: ${subject.classId})`);
  const classUrl = `https://elms.sti.edu/student_class/show/${subject.classId}`;
  await page.goto(classUrl, { waitUntil: 'domcontentloaded', timeout: 20000 });
  await page.waitForTimeout(800);

  const firstLessonUrl = await page.evaluate(() => {
    const a = document.querySelector('a[href*="/student_lesson/show/"]');
    return a ? a.href : null;
  });

  if (!firstLessonUrl) {
    console.log(`   ⚠️ No lesson links found in ${subject.name}.`);
    return [];
  }

  await page.goto(firstLessonUrl, { waitUntil: 'domcontentloaded', timeout: 20000 });
  await page.waitForTimeout(1000);

  // Expand all modules
  await page.evaluate(() => {
    const expandBtn = Array.from(document.querySelectorAll('button, a')).find(el => 
      (el.innerText || '').toLowerCase().includes('expand all')
    );
    if (expandBtn) expandBtn.click();
  }).catch(() => {});
  await page.waitForTimeout(800);

  // Collect handout and syllabus section links
  const sections = await page.evaluate(() => {
    const map = new Map();
    const links = Array.from(document.querySelectorAll('a[href*="section_id="]'));
    links.forEach(a => {
      const text = (a.innerText || '').trim();
      const lower = text.toLowerCase();
      const isHandout = lower.includes('handout') || lower.includes('module handout');
      const isSyllabus = lower.includes('syllabus') || lower.includes('course outline');
      const isActivity = lower.includes('activity') || lower.includes('laboratory') || 
                         lower.includes('exercise') || lower.includes('quiz') || 
                         lower.includes('exam') || lower.includes('task performance');

      if ((isHandout || isSyllabus) && !isActivity) {
        if (!map.has(a.href)) map.set(a.href, { href: a.href, text, isSyllabus });
      }
    });
    return Array.from(map.values());
  });

  console.log(`   🎯 Found ${sections.length} Handout/Syllabus section(s).`);
  const downloadedFiles = [];

  for (let sIdx = 0; sIdx < sections.length; sIdx++) {
    const section = sections[sIdx];
    try {
      await page.goto(section.href, { waitUntil: 'domcontentloaded', timeout: 15000 });
      await page.waitForTimeout(800);

      const fileLinks = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('a'))
          .filter(a => {
            const href = (a.href || '').toLowerCase();
            const text = (a.innerText || '').toLowerCase();
            return (
              href.includes('/files/') ||
              href.endsWith('.pdf') || href.endsWith('.pptx') || href.endsWith('.docx') ||
              text.endsWith('.pdf') || text.endsWith('.pptx') || text.endsWith('.docx')
            );
          })
          .map(a => ({ text: (a.innerText || '').trim(), href: a.href }));
      });

      const targetDir = section.isSyllabus ? syllabiDir : subjectDir;
      if (!fs.existsSync(targetDir)) {
        fs.mkdirSync(targetDir, { recursive: true });
      }

      for (const item of fileLinks) {
        let rawName = item.text || path.basename(new URL(item.href).pathname);
        let fileName = path.basename(rawName).trim();
        // Remove duplicate number tags like (35) before extension
        fileName = fileName.replace(/\([0-9]+\)(?=\.[a-zA-Z0-9]+$)/, '');
        if (!fileName.includes('.')) fileName += '.pdf';
        fileName = fileName.replace(/[/\\?%*:|"<>]/g, '_').trim();
        const filePath = path.join(targetDir, fileName);

        if (fs.existsSync(filePath) && fs.statSync(filePath).size > 0) {
          const sizeKb = (fs.statSync(filePath).size / 1024).toFixed(1);
          telemetry.log(`Cached: ${fileName} (${sizeKb} KB)`, 'info');
          console.log(`     ⏩ Existing: ${fileName} (${sizeKb} KB)`);
          downloadedFiles.push({ file: fileName, status: 'cached', sizeKb });
          continue;
        }

        telemetry.log(`Downloading: ${fileName}...`, 'step');
        console.log(`     ⬇️ Downloading: ${fileName}...`);
        const resp = await page.request.get(item.href, { timeout: 30000 });
        if (resp.ok()) {
          const buffer = await resp.body();
          fs.writeFileSync(filePath, buffer);
          const sizeKb = (buffer.length / 1024).toFixed(1);
          telemetry.log(`Saved: ${fileName} (${sizeKb} KB)`, 'success');
          console.log(`     ✅ Saved: ${fileName} (${sizeKb} KB)`);
          downloadedFiles.push({ file: fileName, status: 'downloaded', sizeKb });
        }
      }
    } catch (err) {
      console.warn(`     ⚠️ Error in section: ${err.message}`);
    }
  }

  return downloadedFiles;
}

export async function runElmsCli(customArgs = null) {
  const args = customArgs || process.argv.slice(2);
  const isHelp = args.includes('--help') || args.includes('-h');
  const isList = args.includes('--list') || args.includes('-l');
  const subjectArg = args.find((a, i) => args[i - 1] === '--subject' || args[i - 1] === '-s');

  if (isHelp) {
    console.log("==========================================================");
    console.log("🎓 STI ELMS SMART AUTOMATION CLI");
    console.log("==========================================================");
    console.log("\nUsage:");
    console.log("  node elms-cli.js --list               # List all enrolled subjects");
    console.log("  node elms-cli.js --subject <name>     # Download handouts for a subject");
    console.log("  node elms-cli.js --all                # Download handouts for all subjects");
    console.log("  node elms-cli.js --help               # Show this help guide");
    return;
  }

  if (isList) {
    console.log("\n📋 Enrolled STI ELMS Subjects:");
    ENROLLED_SUBJECTS.forEach((s, idx) => {
      console.log(`  [${idx + 1}] ${s.name} (Class ID: ${s.classId})`);
    });
    console.log("\nUsage:");
    console.log("  node elms-cli.js --subject \"Game Development\"");
    console.log("  node elms-cli.js --all");
    return;
  }

  console.log("==========================================================");
  console.log("🎓 STI ELMS SMART AUTOMATION CLI");
  console.log("==========================================================");

  const brave = new BraveManager();
  console.log("🪟 Connecting to dedicated background page in Brave...");
  console.log("🛡️  Parallel Co-Browsing Active: Your personal tabs & main window will remain undisturbed.\n");
  const browser = await brave.ensureConnected();
  const ctx = browser.contexts()[0];
  const page = await ctx.newPage();

  try {
    let targetList = ENROLLED_SUBJECTS;
    if (subjectArg) {
      const matched = ENROLLED_SUBJECTS.filter(s => s.name.toLowerCase().includes(subjectArg.toLowerCase()));
      if (matched.length === 0) {
        console.error(`❌ No subject matched query "${subjectArg}". Use --list to view enrolled subjects.`);
        process.exit(1);
      }
      targetList = matched;
    }

    let totalCount = 0;
    telemetry.startTask('elms-handouts', 'Sync Course Handouts', subjectArg || 'All Subjects', targetList.length);

    for (let i = 0; i < targetList.length; i++) {
      const subject = targetList[i];
      telemetry.step(i + 1, targetList.length, `Downloading handouts: ${subject.name}`);
      const files = await downloadSubjectHandouts(page, subject);
      totalCount += files.length;
    }

    telemetry.complete(`Processed ${targetList.length} subject(s) — Total: ${totalCount} handouts`);

    console.log("\n==========================================================");
    console.log(`🎉 Finished processing ${targetList.length} subject(s). Total handouts processed: ${totalCount}`);
    console.log("==========================================================");
  } finally {
    await page.close().catch(() => {});
  }
}

// Auto-run if executed directly as entrypoint
if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  runElmsCli().then(() => {
    process.exit(0);
  }).catch(err => {
    console.error("❌ ELMS CLI Error:", err);
    process.exit(1);
  });
}
