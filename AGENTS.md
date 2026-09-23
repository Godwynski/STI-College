# Student Assistant Instructions & Standards (STI College)

## 🎓 Core Purpose
This workspace contains all STI College academic coursework, handouts, assignments, and exam review materials.

---

## 🛡️ Critical Student Rules

### 1. Strict Assignment Compliance (Zero Fluff)
- **Only do what is asked**: Strictly comply with the assignment/task instructions. Answer only what is asked.
- **NO Self-Grading Rubrics**: Never generate self-awarded evaluation rubrics (e.g., '25/25 Full Points', 'Mastery Standard').
- **NO Unrequested Fluff**: Never add unsolicited executive summaries, decorative callouts, or extraneous files unless explicitly mandated.
- **Single Deliverable**: The primary submission deliverable is `answer.md` inside the module folder. Do not duplicate deliverables.

### 2. Standard Coursework Layout
All academic files must follow this hierarchy:
```
courses/<Subject_Name>/
├── handouts/              # Downloaded lecture slides, PDFs, notes
├── syllabi/               # Course syllabi, grading policies
└── assignments/
    ├── midterm/
    │   └── <Module_Name>/ # e.g., 03_Activity_1, 03_Laboratory_Exercise_1
    │       ├── materials/ # Source PDF handout & prompt
    │       ├── src/       # Executable code (if coding is required)
    │       ├── answer.md  # Final formatted deliverable for submission
    │       └── .tmp/      # Temporary extracted text, scratch files (gitignored)
    └── finals/
```

### 3. Targeted Reading Only (Zero Wandering)
- When working on an assignment, lock your focus strictly to that specific assignment directory: `courses/<Subject>/assignments/<Term>/<Module>/`.
- Do not run exploratory directory scans across unrelated courses or root directories.

### 4. Browser Automation & STI ELMS
- The `brave-control` MCP server connects directly to the user's running Brave browser.
- Use the `sti-elms` skill for batch downloading handouts and submitting assignments on STI ELMS without manual clicking.
- Never launch secondary browser windows; always attach to the running session.
