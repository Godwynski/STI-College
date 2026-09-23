---
name: academic-assignment
description: Autonomous protocol for completing academic coursework, assignments, lab exercises, and activities. Strictly adheres ONLY to what is requested in the task instructions, with zero extraneous additions, no unsolicited files, and no self-awarded grading rubrics.
---

# Academic Assignment Protocol

This skill governs how academic coursework, laboratory exercises, and assignment tasks are solved. It enforces strict compliance with the task prompt to produce authentic, human-grade, clutter-free student deliverables.

---

## 🎯 The Core Directive: Strict Instruction Compliance

> **Rule 1: Only do what is being asked by the instruction of the task file.**  
> **Rule 2: Do NOT add things that are not needed or unrequested.**  
> **Rule 3: Strictly comply to what is being asked.**

When completing any assignment, your job is to fulfill the instructor's exact instructions—**nothing more, nothing less**.

---

## 🚫 Strictly Forbidden Additions (Zero Tolerance)

1. **NO Self-Grading / Rubric Matrices**:
   - The grading rubric in a task handout (e.g., *"The explanation is justified: 5 pts"*) is for the **instructor to evaluate your work**.
   - **NEVER** replicate the rubric inside the submission.
   - **NEVER** award yourself scores (e.g., *"Score: 25/25"*, *"Mastery Standard"*, *"100% Full Points Achieved"*). This makes submissions look artificial and AI-generated.

2. **NO Unsolicited Structural Fluff**:
   - Do **NOT** add "Executive Summaries", "Case Backgrounds", or "Case Summaries Context" unless the task instructions explicitly tell you to write one.
   - Do **NOT** add "Course Objectives", "Key Takeaways", or "Verification & Integrity Summaries" unless requested.
   - Do **NOT** add decorative callout boxes (`> **Key Alignment:** ...`) under questions unless specifically requested by the prompt.

3. **NO Unsolicited Deliverables, Scripts, or Media**:
   - If an assignment asks 4 questions, provide the 4 answers.
   - Do **NOT** create unrequested Python plotting scripts (`generate_deliverables.py`), ASCII charts, data distribution matrices, timeline graphics, demonstration videos (`.mp4`), draw.io files, or zip packages unless the task handout explicitly demands them.
   - Do **NOT** duplicate deliverables (e.g., having both `03_Activity_1.md` and `answer.md` with identical content). The single deliverable is `answer.md`.

---

## 📋 Standard Execution Workflow

### Step 1: Read and Inspect the Task Instructions
1. Locate the source task file in `materials/` (PDF, markdown, or image).
2. Extract the text using Python/CLI into `.tmp/` (never leave extracted text in the root or module directory).
3. Read the prompt thoroughly:
   - What are the exact questions or coding tasks?
   - What is the required deliverable format (Markdown, Word `.docx`, PDF `.pdf`, Python `.py`)?
   - Are there specific constraints, length limits, or file naming conventions?

### Step 2: Formulate Direct, High-Quality Answers
- Address each question or item directly, matching the exact numbers and prompt phrasing used by the teacher.
- Provide strong, clear, technically justified answers that directly satisfy the criteria, without rambling or artificial padding.
- Use clean formatting: bold key terms where helpful for readability, and format lists cleanly.

### Step 3: Produce the Primary Deliverable (`answer.md`)
Save the submission to `answer.md` in the assignment's module directory:
```
courses/<Subject_Name>/assignments/<Term>/<Module_Name>/answer.md
```

#### Markdown Format Reference:
```markdown
**Course Code: <Course_Code> | <Course_Title>**

**<Task_Code>: <Task_Title>**

*Student:* Godwyn Neri | *Date:* <Current_Date>

---

### Direction
<Verbatim direction from the task prompt>

---

### Question 1: <Question Title or Prompt Text>
<Direct, thorough, well-justified response addressing only what is asked.>

---

### Question 2: <Question Title or Prompt Text>
<Direct, thorough, well-justified response addressing only what is asked.>
```

### Step 4: Export to Word / PDF (Only When Needed / Requested)
- If the submission requires a Word document (`.docx`) or PDF (`.pdf`), convert `answer.md` cleanly using the `academic-pdf` skill tools (`render-pdf.js` or `docx_builder.py`).
- Ensure the converted file contains **the exact same content** as `answer.md`—no extra sections, no self-graded rubrics, and no fluff.
