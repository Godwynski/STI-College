---
name: academic-assignment
description: Autonomous protocol for completing academic coursework, assignments, lab exercises, and activities. Answers are always as simple as possible, easy to understand, and concise, strictly following task instructions with zero extraneous additions, no unsolicited files, and no self-awarded grading rubrics.
---

# Academic Assignment Protocol

This skill governs how academic coursework, laboratory exercises, and assignment tasks are solved. It enforces strict compliance with the task prompt to produce simple, concise, easy-to-understand, and clutter-free student deliverables.

---

## 🎯 The Core Directive: Strict Instruction Compliance & Maximum Simplicity

> **Rule 1: Strictly comply to what is being asked by the instruction of the task file.**  
> **Rule 2: Keep answers as simple as possible, easy to understand, and concise.**  
> **Rule 3: Only do what is being asked—do NOT add unrequested or unnecessary content.**

When completing any assignment, your job is to fulfill the instructor's exact instructions—**nothing more, nothing less**—delivering direct, plain-language answers without fluff or over-complication.

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

4. **NO Overcomplicated Language or Jargon Bloat**:
   - Do **NOT** use convoluted academic phrasing, run-on sentences, or decorative buzzwords to artificially pad an answer.
   - Never use ten words when five will convey the concept cleanly and accurately.

---

## ✍️ Writing Standard: Simple, Understandable, & Concise

- **Maximum Simplicity:** Write in plain, direct language that anyone can easily follow. Break down technical concepts without using unnecessary jargon.
- **Easy to Understand:** Focus on clarity. Keep explanations logical and organized, using brief bullet points or short paragraphs where appropriate.
- **Strictly Concise:** Eliminate preamble, filler phrases, and repetitive explanations. Get straight to the answer.
- **Strict Prompt Scope:** Never exceed what the prompt asks for. If the question asks for 2 reasons, give exactly 2 clear reasons. If a brief explanation is requested, do not write multiple lengthy paragraphs.

---

## 📋 Standard Execution Workflow

### Step 1: Read and Inspect the Task Instructions
1. Locate the source task file in `materials/` (PDF, markdown, or image).
2. Extract the text using Python/CLI into `.tmp/` (never leave extracted text in the root or module directory).
3. Read the prompt thoroughly:
   - What are the exact questions or coding tasks?
   - What is the required deliverable format (Markdown, Word `.docx`, PDF `.pdf`, Python `.py`)?
   - Are there specific constraints, length limits, or file naming conventions?

### Step 2: Formulate Simple, Concise, and Direct Answers
- Address each question or item directly, matching the exact numbers and prompt phrasing used by the teacher.
- Keep the language **as simple and easy to understand as possible** while maintaining technical accuracy.
- Keep answers **strictly concise**: avoid rambling, wordiness, or artificial padding.
- Strictly fulfill the instruction criteria—do not guess or provide unsolicited extra topics.
- Use clean formatting: bold key terms where helpful for quick scanning, and format lists cleanly.

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
