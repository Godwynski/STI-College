# Student Assistant Instructions & Standards: STI College

## 🎓 Workspace Overview & Purpose
This workspace is the dedicated repository for all **STI College** academic coursework, laboratory exercises, performance tasks, handouts, and exam reviewers for **Godwyn Neri**.

### 📚 Enrolled Subjects & Courses
- **`Computer_Graphics_Programming`** (CGP)
- **`Euthenics_2`**
- **`Game_Development`** (GD)
- **`IT_Capstone_Project_2`** (Capstone)
- **`IT_Service_Management`** (ITSM / ITIL)
- **`Information_Assurance_and_Security`** (IAS / AWS Cloud)
- **`Network_Technology_2`** (NetTech 2 / Cisco / VPC)

---

## 🏛️ Standard Coursework Directory Structure

Every academic module, exercise, and assignment MUST adhere to this structure:

```
courses/<Subject_Name>/
├── handouts/              # Downloaded lecture slides, PDFs, notes
├── syllabi/               # Course syllabi, grading policies
└── assignments/
    ├── midterm/
    │   └── <Module_Name>/ # e.g., 03_Activity_1, 03_Laboratory_Exercise_1
    │       ├── materials/ # Source PDF handout, prompts, teacher diagrams
    │       ├── src/       # Executable source code (e.g., Python, C++, JS, Draw.io)
    │       ├── answer.md  # Primary human-grade submission report
    │       └── .tmp/      # Temporary OCR/extracted text (gitignored)
    └── finals/
```

---

## 🛡️ Critical Student Rules (Zero Tolerance)

### 1. Strict Assignment Compliance (Zero Fluff)
- **Fulfill the prompt—nothing more, nothing less**: Answer only what is asked by the teacher's instructions.
- **NO Self-Grading Rubrics**: The grading rubric in the handout is for the instructor, not the student. NEVER insert self-awarded evaluation matrices (e.g., *"Score: 25/25 Full Points"*, *"Mastery Standard Achieved"*). This makes submissions look artificial and AI-generated.
- **NO Unsolicited Structural Fluff**: Never add unrequested executive summaries, decorative callouts, or extraneous files unless explicitly mandated by the task handout.
- **Single Deliverable**: The primary written submission is `answer.md` inside the module folder. Do not generate duplicate deliverable names (e.g., do not keep both `03_Activity_1.md` and `answer.md`).

### 2. Targeted Reading Only (Zero Wandering)
- When solving an assignment or answering a question, **lock your scope strictly** to that specific assignment folder: `courses/<Subject>/assignments/<Term>/<Module>/`.
- **NEVER** run exploratory directory listings across unrelated courses, root folders, or external project directories.
- Read only the assignment prompt in `materials/` and the active deliverable files.

---

## ⚡ Built-in Academic Skills (`.agents/skills/`)

This workspace includes 3 autonomous student skills to streamline schoolwork:

| Skill | Purpose | How to Use |
| :--- | :--- | :--- |
| **`academic-assignment`** | Solves assignments with strict prompt compliance and zero artificial fluff | Activate when asked to answer an exercise, lab, or task handout |
| **`academic-pdf`** | Generates clean, publication-grade monochrome PDF & Word deliverables | Activate to convert `answer.md` into `answer.pdf` or `.docx` |
| **`sti-elms`** | Fast batch downloader for course handouts, syllabi, and assignment PDFs | Uses global `brave-control` MCP to scrape/download materials automatically |

---

## 🌐 Browser Automation & STI ELMS Bridge

The user's Brave browser runs with remote debugging enabled. The global MCP server **`brave-control`** connects Antigravity directly to the user's active session without needing local MCP server files.

- Use `sti-elms` or `brave-control` to check upcoming deadlines, navigate STI ELMS, and download new module materials directly into `materials/`.
- **NEVER** launch a secondary browser window or new browser profile (`AgentProfile`); always connect to the running browser session.

---

## 📝 Deliverable Formatting Template (`answer.md`)

```markdown
**Course Code: <Course_Code> | <Course_Title>**

**<Task_Code>: <Task_Title>**

*Student:* Godwyn Neri | *Date:* <Current_Date>

---

### Direction
<Verbatim instructions from the task handout>

---

### Question 1: <Question Title or Prompt Text>
<Direct, thorough, technically justified answer satisfying the criteria.>

---
```
