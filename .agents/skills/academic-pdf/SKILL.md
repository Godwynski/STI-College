---
name: academic-pdf
description: Generates clean, minimalist, print-friendly academic PDFs and Word documents for school submissions following strict monochrome typography, minimal accent rules, and strict adherence to task instructions without unrequested fluff.
---

# Academic PDF & Document Skill Guide

This skill provides an automated workflow and strict design system for creating **clean, minimalist, print-friendly academic PDFs and Word documents** for coursework, lab reports, activities, and school deliverables.

---

## 🎯 STRICT INSTRUCTION COMPLIANCE (ANTI-BLOAT PROTOCOL)

> **Rule 1: Only do what is being asked by the instruction of the task file.**  
> **Rule 2: Do NOT add things that are not needed or unrequested.**  
> **Rule 3: Strictly comply to what is being asked.**

### 🚫 Strictly Forbidden in Deliverables:
1. **NO Self-Graded Rubrics**:
   - The grading rubric on the task sheet is for the instructor, NOT the student.
   - **Never** add a "Grading Rubric Alignment Table", "Rubric Compliance Matrix", or score declarations (`25/25`, `Mastery Standard`).
2. **NO Unsolicited Fluff Sections**:
   - Do **NOT** add "Executive Summaries", "Case Background Overviews", "Course Objectives", or "Key Takeaways" unless the assignment prompt explicitly requires them.
3. **NO Unsolicited Visual Additions**:
   - Do **NOT** inject decorative callout boxes under every question unless a warning or prerequisite is genuinely required by the task prompt.
   - Do **NOT** generate unrequested ASCII charts, bar graphs, timeline diagrams, videos, or draw.io diagrams unless explicitly demanded by the instructions.
4. **NO Unrequested Secondary Files**:
   - Do not litter the workspace with extra Python generation scripts (`generate_deliverables.py`), duplicate markdown files (`03_Activity_1.md` alongside `answer.md`), or zip files unless explicitly requested.

---

## 🎨 Core Design System: "Color Only When Needed"

The design strips away heavy colored banners, solid header fills, and decorative container shading. Color is strictly treated as a **functional signal**, never as decorative background styling.

### Palette Tokens
| Token | Hex Value | Role & Usage |
| :--- | :---: | :--- |
| **Canvas / Background** | `#FFFFFF` | Crisp pure white. No full-page tints or colored cards. |
| **Typography** | `#4A4A4A` | High-contrast charcoal for all titles, headers, and body text. Prints sharp without harsh pure black glare. |
| **Functional Accent** | `#E2B4BD` | Reserved strictly for critical signals: callout left border, subtle header divider, and status badges. |
| **Header Border** | `#4A4A4A` | Fine 1px–1.5px horizontal rule directly beneath table column headers. |
| **Row Divider** | `#EEEEEE` | Subtle hairline divider between table rows. |
| **Muted Meta** | `#718096` | Subdued metadata (date, instructor, course details). |

---

## 📐 The Four Minimalist Visual Rules

### 1. Default to Clean Monochrome
* **Canvas:** Pure white (`#FFFFFF`) with standard 1-inch margins. Never apply gradient or tinted backgrounds.
* **Typography:** Charcoal (`#4A4A4A`) for all textual content.
* **Font Family:** System native sans-serif (`-apple-system`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial`) or serif (`Georgia`, `Times New Roman`) with 1.5–1.6 line height.

### 2. Tables Without Solid Color Fills (When Tables Are Requested)
* **No solid filled banner headers** (no navy, blue, or dark grey header blocks).
* **No alternating striped rows** (zebra stripes are eliminated).
* **Clear Border Hierarchy:**
  * Top of table: None.
  * Below column headers: Fine 1px–1.5px line in `#4A4A4A`.
  * Row separators: Ultra-fine 1px `#EEEEEE` line.
  * Bottom of table: 1px subtle closing rule in `#D0D0D0`.
* **Ample Padding:** Generous vertical padding (`10px–14px`) ensures effortless scanning.

### 3. Where the Accent (`#E2B4BD`) is Used
The accent color is strictly applied to three functional elements only:
1. **Critical Callouts Only:** A single, thin 2px–3px left accent border beside a genuine constraint or warning (when required).
2. **Status Badges / Key Markers:** Small, subtle inline text labels (e.g., `[PASS]`, `[PENDING]`) styled with a fine `#E2B4BD` border.
3. **Subtle Header Dividers:** A thin 1px horizontal rule under the document title to cleanly separate header metadata from the document body.

### 4. Structure via Spacing
* Structure sections through generous whitespace (`20px–32px` vertical margin) and typographic hierarchy rather than boxed cards or shaded containers.

---

## 🛠️ Automated Tools & Generators

The skill includes pre-built tools in its `scripts/` directory:

### 1. Zero-Token CLI: Markdown/HTML to PDF via Brave CDP
Converts any markdown file or HTML template into a vector, print-ready PDF using the connected Brave browser engine:

```bash
node .agents/skills/academic-pdf/scripts/render-pdf.js --input <path/to/document.md> --output <path/to/output.pdf>
```

*Example:*
```bash
node .agents/skills/academic-pdf/scripts/render-pdf.js --input courses/IT_Service_Management/assignments/midterm/03_Activity_1/answer.md --output courses/IT_Service_Management/assignments/midterm/03_Activity_1/03_Activity_1_Godwyn_Neri.pdf
```

### 2. Python DOCX Generator: Minimalist Word Submissions
When Microsoft Word (`.docx`) is required, use `AcademicDocBuilder` from `docx_builder.py`:

```python
from scripts.docx_builder import AcademicDocBuilder

builder = AcademicDocBuilder(
    title="03 Activity 1: ITSM Processes and ITIL Principles",
    course_code="IT2312 | IT Service Management",
    student_name="Godwyn Neri",
    date_str="September 24, 2026"
)

builder.add_heading("Direction", level=1)
builder.add_paragraph("Elaborate on the correlation between the purposes of ITSM Processes and ITIL Principles.")

builder.add_heading("Question 1: In which ITSM Process would the Progress Iteratively with Feedback principle apply best?", level=2)
builder.add_paragraph("The ITIL principle 'Progress Iteratively with Feedback' applies best to the Continual Service Improvement (CSI) process...")

builder.save("output_document.docx")
```

---

## 📝 Markdown Authoring Template (Direct Q&A)

When authoring `answer.md` for school assignments, strictly follow this direct structure:

```markdown
**Course Code: <Course_Code> | <Course_Title>**

**<Task_Code>: <Task_Title>**

*Student:* Godwyn Neri | *Date:* <Current_Date>

---

### Direction
<Verbatim directions from the task file>

---

### Question 1: <Exact question prompt>
<Direct, thorough, justified answer addressing only what was asked.>

---

### Question 2: <Exact question prompt>
<Direct, thorough, justified answer addressing only what was asked.>
```

---

## 📂 File Structure

```text
.agents/skills/academic-pdf/
├── SKILL.md                          # Standards guide (strict compliance + minimalist aesthetics)
├── scripts/
│   ├── render-pdf.js                 # CLI to render Markdown/HTML to PDF via CDP
│   └── docx_builder.py               # Minimalist Word .docx generator
├── templates/
│   └── academic-style.css            # Print-ready CSS implementing all rules
└── examples/
    ├── sample-activity.md            # Reference markdown deliverable
    ├── sample-activity.pdf           # Rendered reference PDF
    └── sample-activity.docx          # Rendered reference Word document
```
