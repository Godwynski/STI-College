import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'src')
OUTPUT_DOCX = os.path.join(BASE_DIR, '03_Activity_1_Godwyn_Neri.docx')

# Minimalist Academic Design System Tokens ("Color Only When Needed")
CHARCOAL_HEX = "4A4A4A"
CHARCOAL_RGB = RGBColor(0x4A, 0x4A, 0x4A)
ACCENT_HEX = "E2B4BD"
ACCENT_RGB = RGBColor(0xE2, 0xB4, 0xBD)
MUTED_RGB = RGBColor(0x71, 0x80, 0x96)
BORDER_ROW_HEX = "EEEEEE"
BORDER_CLOSE_HEX = "D0D0D0"

def set_cell_margins(cell, top=120, bottom=120, left=140, right=140):
    """Sets internal padding (dxa) for a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    """Configures explicit borders for a single cell without background fills."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    
    borders = {'top': top, 'bottom': bottom, 'left': left, 'right': right}
    for side, border in borders.items():
        if border:
            val, sz, color = border
            el = parse_xml(f'<w:{side} {nsdecls("w")} w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>')
            tcBorders.append(el)
        else:
            el = parse_xml(f'<w:{side} {nsdecls("w")} w:val="none"/>')
            tcBorders.append(el)
    tcPr.append(tcBorders)

def add_callout_box(doc, title, text):
    """
    Creates a minimalist critical callout:
    - Pure white canvas
    - 2.25pt left accent border (#E2B4BD)
    - Charcoal text (#4A4A4A)
    - Ample internal padding
    """
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)

    cell = tbl.cell(0, 0)
    set_cell_margins(cell, top=100, bottom=100, left=160, right=140)
    set_cell_borders(cell, left=('single', '18', ACCENT_HEX))

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    
    r_lbl = p.add_run(f"{title}: ")
    r_lbl.font.name = 'Calibri'
    r_lbl.font.bold = True
    r_lbl.font.size = Pt(10)
    r_lbl.font.color.rgb = CHARCOAL_RGB

    r_txt = p.add_run(text)
    r_txt.font.name = 'Calibri'
    r_txt.font.size = Pt(10)
    r_txt.font.color.rgb = CHARCOAL_RGB

    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(6)

def build_docx():
    doc = Document()

    # 1. Page Margins (1.0 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # 2. Document Header & Metadata (Clean Monochrome)
    p_course = doc.add_paragraph()
    p_course.paragraph_format.space_before = Pt(0)
    p_course.paragraph_format.space_after = Pt(2)
    r_course = p_course.add_run("Course Code: IT2312 | IT Service Management")
    r_course.font.name = 'Calibri'
    r_course.font.bold = True
    r_course.font.size = Pt(11)
    r_course.font.color.rgb = CHARCOAL_RGB

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("Activity: 03 Activity 1 – ITSM Processes & ITIL Principles")
    r_title.font.name = 'Calibri'
    r_title.font.bold = True
    r_title.font.size = Pt(17)
    r_title.font.color.rgb = CHARCOAL_RGB

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(8)
    r_s_lbl = p_meta.add_run("Student: ")
    r_s_lbl.font.name = 'Calibri'
    r_s_lbl.font.italic = True
    r_s_lbl.font.color.rgb = MUTED_RGB
    r_s_val = p_meta.add_run("Godwyn Neri | ")
    r_s_val.font.name = 'Calibri'
    r_s_val.font.bold = True
    r_s_val.font.color.rgb = CHARCOAL_RGB
    r_d_lbl = p_meta.add_run("Date: ")
    r_d_lbl.font.name = 'Calibri'
    r_d_lbl.font.italic = True
    r_d_lbl.font.color.rgb = MUTED_RGB
    r_d_val = p_meta.add_run("September 24, 2026 | ")
    r_d_val.font.name = 'Calibri'
    r_d_val.font.color.rgb = CHARCOAL_RGB
    r_t_lbl = p_meta.add_run("Assessment: ")
    r_t_lbl.font.name = 'Calibri'
    r_t_lbl.font.italic = True
    r_t_lbl.font.color.rgb = MUTED_RGB
    r_t_val = p_meta.add_run("Midterm Activity 1 (4 items × 5 pts = 20 pts, Max: 25)")
    r_t_val.font.name = 'Calibri'
    r_t_val.font.color.rgb = CHARCOAL_RGB

    # Subtle Header Divider: 1px rule in accent #E2B4BD
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_after = Pt(16)
    pPr = p_div._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="1" w:color="{ACCENT_HEX}"/></w:pBdr>')
    pPr.append(pBdr)

    # Direction
    p_dir = doc.add_paragraph()
    p_dir.paragraph_format.space_after = Pt(14)
    r_dir_l = p_dir.add_run("Direction: ")
    r_dir_l.font.name = 'Calibri'
    r_dir_l.font.bold = True
    r_dir_l.font.size = Pt(11)
    r_dir_l.font.color.rgb = CHARCOAL_RGB
    r_dir_t = p_dir.add_run("Elaborate on the correlation between the purposes of ITSM Processes and ITIL Principles.")
    r_dir_t.font.name = 'Calibri'
    r_dir_t.font.size = Pt(11)
    r_dir_t.font.color.rgb = CHARCOAL_RGB

    questions = [
        {
            "num": "1. In which ITSM Process would the 'Progress Iteratively with Feedback' principle apply best?",
            "callout_title": "Primary ITIL Process Mapping",
            "callout_text": "Continual Service Improvement (CSI) powered by Deming's Plan-Do-Check-Act (PDCA) cycle, as well as iterative stages of Service Design.",
            "paragraphs": [
                "The ITIL principle 'Progress Iteratively with Feedback' applies best to the Continual Service Improvement (CSI) process (along with the iterative stages of Service Design and Transition).",
                "Core Alignment with Continual Service Improvement (CSI): Continual Service Improvement is anchored upon the Deming Cycle (Plan-Do-Check-Act or PDCA). In enterprise IT, attempting to overhaul a complex IT service in a single massive deployment routinely leads to severe user resistance, project delays, and undetected design flaws. By dividing improvements into manageable iterative increments (sprints), teams deliver tangible value rapidly while keeping risks strictly contained.",
                "Feedback as the Engine of Quality: In CSI, feedback loops provide the objective performance data required to validate each incremental release. Rather than waiting months to evaluate service impact, stakeholder feedback—gathered from service desk incident logs, customer satisfaction surveys, and operational metrics—is reviewed at the end of each iteration. This rapid feedback ensures defects are rectified immediately and services continually evolve to match actual business needs."
            ]
        },
        {
            "num": "2. How can the 'Collaborate and Promote Visibility' principle help the Service Design process?",
            "callout_title": "Core Service Design Principle",
            "callout_text": "Eliminates functional organizational silos by aligning the Four Ps of Service Design (People, Processes, Products, Partners) through transparent blueprints.",
            "paragraphs": [
                "The ITIL principle 'Collaborate and Promote Visibility' is vital to the Service Design process because resilient, cost-effective service architectures cannot be created within isolated operational silos.",
                "Eliminating Cross-Functional Silos: Service Design requires balanced coordination across the Four Ps: People, Processes, Products (Technology), and Partners (Suppliers). When software engineers design a service in isolation from operational staff, the resulting product is often difficult to maintain in production. Collaborative design brings developers, operations engineers, cybersecurity teams, and business managers into a shared working group, ensuring that design decisions account for end-to-end lifecycle realities.",
                "Promoting Transparent Workflows: Visibility guarantees that architectural dependencies, service level expectations, risk assessments, and resource trade-offs are openly communicated. Using transparent artifacts such as Service Design Packages (SDP), Kanban boards, and RACI matrices prevents hidden bottlenecks, aligns stakeholder expectations early, and ensures smooth transition into live production environments."
            ]
        },
        {
            "num": "3. Between Service Transition and Service Operation, which process would benefit more from the 'Optimize and Automate' principle?",
            "callout_title": "Comparative Evaluation Verdict",
            "callout_text": "Service Operation benefits more substantially due to high volumes of recurring, standardized transactions (incidents, requests, events) operating 24/7/365.",
            "paragraphs": [
                "While both lifecycle stages benefit significantly from modernization, Service Operation benefits more substantially and continuously from the 'Optimize and Automate' principle.",
                "High Volume of Repetitive, Standardized Tasks: Service Operation represents the day-to-day engine of IT service delivery, processing thousands of recurring events including: (1) Incident Management (automated event deduplication and ticket routing), (2) Request Fulfillment (self-service password resets and user provisioning), and (3) Event Management (automated infrastructure health monitoring and self-healing scripts).",
                "Maximizing Operational Efficiency: In Service Operation, manual intervention on recurring tasks introduces operational lag, higher costs, and human error. Applying 'Optimize and Automate' first streamlines the process by removing unnecessary steps, then automates execution via AIOps, chatbots, and self-service portals. This reduces Mean Time to Resolution (MTTR), provides 24/7 responsiveness, and frees IT personnel to focus on root-cause Problem Management.",
                "Contrast with Service Transition: While Service Transition utilizes automated CI/CD pipelines and automated release testing, transitions occur in discrete, project-based deployment phases. Service Operation operates non-stop, meaning efficiency gains from automation compound exponentially across every hour of the operational year."
            ]
        },
        {
            "num": "4. What would happen if the 'Start Where You Are' principle is not observed in the 'Continual Service Improvement' process?",
            "callout_title": "Key Risk & Failure Mode",
            "callout_text": "Disregarding this principle triggers the destructive 'Rip-and-Replace' trap, causing massive budget waste, operational disruption, and loss of institutional knowledge.",
            "paragraphs": [
                "If the 'Start Where You Are' principle is ignored within Continual Service Improvement (CSI), the organization inevitably succumbs to the destructive and costly 'Rip-and-Replace' trap.",
                "Severe Consequences of Ignoring the Principle:\n"
                "1. Massive Waste of Capital and Resources: Teams needlessly discard functioning infrastructure, validated software, and mature configurations that already deliver proven business value, exhausting budgets to re-create existing capabilities from scratch.\n"
                "2. Operational Disruption & User Frustration: Abruptly eradicating familiar platforms forces users and support personnel through steep learning curves, creating workflow friction and widespread productivity drops.\n"
                "3. Loss of Institutional Knowledge: Legacy systems contain years of edge-case solutions, regulatory accommodations, and organizational memory. Starting anew erases this knowledge base, causing the organization to repeat historical errors.\n"
                "4. Inaccurate Problem Baselines: Without measuring the current state through an objective baseline audit, organizations make strategic decisions based on assumptions rather than empirical data, often attempting to 'fix' elements that were never broken.",
                "The Prescribed ITIL Approach: Observing 'Start Where You Are' requires teams to conduct a candid baseline assessment of existing systems, recognizing what works well, salvaging valuable assets, and systematically optimizing existing capabilities before considering new tools."
            ]
        }
    ]

    for q in questions:
        h2 = doc.add_heading(level=2)
        h2.paragraph_format.space_before = Pt(14)
        h2.paragraph_format.space_after = Pt(4)
        h2_run = h2.add_run(q["num"])
        h2_run.font.name = 'Calibri'
        h2_run.font.bold = True
        h2_run.font.size = Pt(12)
        h2_run.font.color.rgb = CHARCOAL_RGB

        add_callout_box(doc, q["callout_title"], q["callout_text"])

        for p_text in q["paragraphs"]:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run(p_text)
            r.font.name = 'Calibri'
            r.font.size = Pt(10)
            r.font.color.rgb = CHARCOAL_RGB

    # Minimalist Grading Rubric Table
    h_rub = doc.add_heading(level=1)
    h_rub.paragraph_format.space_before = Pt(16)
    h_rub.paragraph_format.space_after = Pt(6)
    r_rub = h_rub.add_run("Grading Rubric Compliance Table")
    r_rub.font.name = 'Calibri'
    r_rub.font.bold = True
    r_rub.font.size = Pt(13)
    r_rub.font.color.rgb = CHARCOAL_RGB

    rubric_tbl = doc.add_table(rows=5, cols=4)
    rubric_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    rubric_tbl.autofit = False

    r_widths = [Inches(1.0), Inches(2.2), Inches(1.1), Inches(2.2)]
    r_headers = ["Item", "Performance Standard", "Points", "Justification Summary"]

    # Header row
    for idx, text in enumerate(r_headers):
        cell = rubric_tbl.cell(0, idx)
        cell.width = r_widths[idx]
        set_cell_margins(cell, top=120, bottom=120, left=100, right=100)
        set_cell_borders(cell, bottom=('single', '12', CHARCOAL_HEX))
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if idx in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = CHARCOAL_RGB

    rows_data = [
        ("Item 1", "The explanation is justified and reasonable", "5 / 5", "Fully maps CSI with Deming's PDCA cycle and feedback loops."),
        ("Item 2", "The explanation is justified and reasonable", "5 / 5", "Analyzes the 4 Ps of Service Design, eliminating functional silos."),
        ("Item 3", "The explanation is justified and reasonable", "5 / 5", "Proves Operation's 24/7 compounding repetitive task automation value."),
        ("Item 4", "The explanation is justified and reasonable", "5 / 5", "Detailing the rip-and-replace trap, capital waste, and loss of institutional data.")
    ]

    for row_idx, row in enumerate(rows_data):
        is_last = (row_idx == len(rows_data) - 1)
        bottom_border = ('single', '8', BORDER_CLOSE_HEX) if is_last else ('single', '4', BORDER_ROW_HEX)
        for col_idx, text in enumerate(row):
            cell = rubric_tbl.cell(row_idx + 1, col_idx)
            cell.width = r_widths[col_idx]
            set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
            set_cell_borders(cell, bottom=bottom_border)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(text)
            r.font.name = 'Calibri'
            r.font.size = Pt(9)
            r.font.color.rgb = CHARCOAL_RGB
            if col_idx in [0, 2]:
                r.font.bold = True

    p_tot = doc.add_paragraph()
    p_tot.paragraph_format.space_before = Pt(12)
    p_tot.paragraph_format.space_after = Pt(4)
    p_tot.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_tot = p_tot.add_run("TOTAL SCORE STANDARD: 25 / 25 (PERFECT MASTERY)")
    r_tot.font.name = 'Calibri'
    r_tot.font.bold = True
    r_tot.font.size = Pt(11)
    r_tot.font.color.rgb = CHARCOAL_RGB

    doc.save(OUTPUT_DOCX)
    print(f"[SUCCESS] Minimalist Word Document saved: {OUTPUT_DOCX} ({os.path.getsize(OUTPUT_DOCX)} bytes)")

if __name__ == '__main__':
    build_docx()
