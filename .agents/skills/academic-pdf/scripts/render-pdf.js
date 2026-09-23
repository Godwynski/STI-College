import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { BraveManager } from '../../../../brave-mcp/src/browser.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const CSS_TEMPLATE_PATH = path.join(__dirname, '../templates/academic-style.css');

/**
 * Lightweight, zero-dependency Markdown-to-HTML converter designed specifically
 * for academic documents following the "Color Only When Needed" guidelines.
 */
export function markdownToAcademicHtml(mdContent, options = {}) {
  const css = fs.readFileSync(CSS_TEMPLATE_PATH, 'utf-8');
  const lines = mdContent.split(/\r?\n/);
  
  let htmlBody = '';
  let inTable = false;
  let tableHeaderParsed = false;
  let inBlockquote = false;
  let blockquoteContent = [];
  let inList = false;
  let listType = 'ul';

  function closeList() {
    if (inList) {
      htmlBody += `</${listType}>\n`;
      inList = false;
    }
  }

  function closeTable() {
    if (inTable) {
      htmlBody += `</tbody></table>\n`;
      inTable = false;
      tableHeaderParsed = false;
    }
  }

  function closeBlockquote() {
    if (inBlockquote) {
      const text = blockquoteContent.join(' ').trim();
      htmlBody += `<blockquote>${formatInline(text)}</blockquote>\n`;
      inBlockquote = false;
      blockquoteContent = [];
    }
  }

  function formatInline(text) {
    // Badges like [PASS], [PENDING], [VERIFIED]
    let res = text.replace(/\[(PASS|PENDING|VERIFIED|DONE|FAIL|WARN)\]/gi, (match, p1) => {
      return `<span class="badge badge-accent">${p1.toUpperCase()}</span>`;
    });

    // Inline code
    res = res.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Bold
    res = res.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

    // Italic
    res = res.replace(/\*([^*]+)\*/g, '<em>$1</em>');

    return res;
  }

  for (let i = 0; i < lines.length; i++) {
    const rawLine = lines[i];
    const line = rawLine.trim();

    // Check for Horizontal Rule
    if (line.match(/^(?:---|___|\*\*\*)$/)) {
      closeList();
      closeTable();
      closeBlockquote();
      htmlBody += `<hr class="header-divider">\n`;
      continue;
    }

    // Check for Blockquote
    if (line.startsWith('>')) {
      closeList();
      closeTable();
      inBlockquote = true;
      blockquoteContent.push(line.replace(/^>\s*/, ''));
      continue;
    } else if (inBlockquote) {
      closeBlockquote();
    }

    // Check for Table Row
    if (line.startsWith('|') && line.endsWith('|')) {
      closeList();
      closeBlockquote();
      const cells = line.split('|').slice(1, -1).map(c => c.trim());

      // Check if it's separator row |---|---|
      if (cells.every(c => c.match(/^:?-+:?$/))) {
        tableHeaderParsed = true;
        continue;
      }

      if (!inTable) {
        inTable = true;
        tableHeaderParsed = false;
        htmlBody += `<table>\n<thead>\n<tr>`;
        cells.forEach(c => {
          htmlBody += `<th>${formatInline(c)}</th>`;
        });
        htmlBody += `</tr>\n</thead>\n<tbody>\n`;
      } else {
        htmlBody += `<tr>`;
        cells.forEach(c => {
          htmlBody += `<td>${formatInline(c)}</td>`;
        });
        htmlBody += `</tr>\n`;
      }
      continue;
    } else if (inTable) {
      closeTable();
    }

    // Check for Headings
    const headingMatch = line.match(/^(#{1,6})\s+(.*)$/);
    if (headingMatch) {
      closeList();
      closeTable();
      closeBlockquote();
      const level = headingMatch[1].length;
      const text = formatInline(headingMatch[2]);
      htmlBody += `<h${level}>${text}</h${level}>\n`;
      continue;
    }

    // Check for Unordered List
    const ulMatch = line.match(/^[-*]\s+(.*)$/);
    if (ulMatch) {
      closeTable();
      closeBlockquote();
      if (!inList || listType !== 'ul') {
        closeList();
        inList = true;
        listType = 'ul';
        htmlBody += `<ul>\n`;
      }
      htmlBody += `<li>${formatInline(ulMatch[1])}</li>\n`;
      continue;
    }

    // Check for Ordered List
    const olMatch = line.match(/^\d+\.\s+(.*)$/);
    if (olMatch) {
      closeTable();
      closeBlockquote();
      if (!inList || listType !== 'ol') {
        closeList();
        inList = true;
        listType = 'ol';
        htmlBody += `<ol>\n`;
      }
      htmlBody += `<li>${formatInline(olMatch[1])}</li>\n`;
      continue;
    }

    // Normal empty line
    if (!line) {
      closeList();
      closeTable();
      closeBlockquote();
      continue;
    }

    // Normal Paragraph
    closeList();
    closeTable();
    closeBlockquote();
    htmlBody += `<p>${formatInline(line)}</p>\n`;
  }

  closeList();
  closeTable();
  closeBlockquote();

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>${options.title || 'Academic Submission'}</title>
  <style>
${css}
  </style>
</head>
<body>
${htmlBody}
</body>
</html>`;
}

/**
 * Renders HTML/Markdown content to a high-quality, print-friendly PDF via Brave CDP.
 */
export async function generateAcademicPdf({ inputPath, outputPath, htmlContent = null }) {
  let finalHtml = htmlContent;

  if (!finalHtml && inputPath) {
    const raw = fs.readFileSync(path.resolve(inputPath), 'utf-8');
    if (inputPath.endsWith('.html')) {
      finalHtml = raw;
    } else {
      finalHtml = markdownToAcademicHtml(raw, {
        title: path.basename(inputPath, path.extname(inputPath))
      });
    }
  }

  if (!finalHtml) {
    throw new Error('No content or inputPath provided for PDF generation.');
  }

  // Connect via BraveManager
  const manager = new BraveManager();
  const page = await manager.getAgentPage();

  // Load the rendered HTML into page
  await page.setContent(finalHtml, { waitUntil: 'load' });
  await page.waitForTimeout(300);

  // Capture print-ready PDF using CDP Page.printToPDF
  const cdp = await page.context().newCDPSession(page);
  const result = await cdp.send('Page.printToPDF', {
    printBackground: true,
    paperWidth: 8.5,
    paperHeight: 11,
    marginTop: 0.8,
    marginBottom: 0.8,
    marginLeft: 0.8,
    marginRight: 0.8,
    preferCSSPageSize: true
  });

  const pdfBuffer = Buffer.from(result.data, 'base64');
  const targetPath = path.resolve(outputPath);
  fs.mkdirSync(path.dirname(targetPath), { recursive: true });
  fs.writeFileSync(targetPath, pdfBuffer);

  console.log(`✅ Academic PDF created: ${targetPath} (${(pdfBuffer.length / 1024).toFixed(1)} KB)`);
  return targetPath;
}

// CLI Execution Support
if (process.argv[1] && process.argv[1].endsWith('render-pdf.js')) {
  const args = process.argv.slice(2);
  const inputIdx = args.findIndex(a => a === '--input' || a === '-i');
  const outputIdx = args.findIndex(a => a === '--output' || a === '-o');

  if (inputIdx === -1 || outputIdx === -1) {
    console.log("Usage: node render-pdf.js --input <file.md|file.html> --output <file.pdf>");
    process.exit(1);
  }

  const inputPath = args[inputIdx + 1];
  const outputPath = args[outputIdx + 1];

  generateAcademicPdf({ inputPath, outputPath })
    .then(() => process.exit(0))
    .catch(err => {
      console.error("PDF generation failed:", err);
      process.exit(1);
    });
}
