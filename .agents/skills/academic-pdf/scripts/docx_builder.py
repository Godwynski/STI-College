"""
Minimalist Academic DOCX Builder
Adheres strictly to the "Color Only When Needed" guidelines:
- Canvas: Pure White (#FFFFFF)
- Typography: Charcoal (#4A4A4A)
- Tables: No solid fills or alternating stripes; fine 1px header bottom border; ample vertical padding
- Accent (#E2B4BD): Critical callout left border, subtle divider, status badges
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

CHARCOAL_HEX = "4A4A4A"
CHARCOAL_RGB = RGBColor(0x4A, 0x4A, 0x4A)
ACCENT_HEX = "E2B4BD"
ACCENT_RGB = RGBColor(0xE2, 0xB4, 0xBD)
MUTED_RGB = RGBColor(0x71, 0x80, 0x96)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
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
    """Configures explicit borders for a single cell."""
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

class AcademicDocBuilder:
    def __init__(self, title, course_code, student_name="Godwyn Neri", date_str="September 24, 2026"):
        self.doc = Document()
        self.title = title
        self.course_code = course_code
        self.student_name = student_name
        self.date_str = date_str
        self._configure_margins()
        self._add_header()

    def _configure_margins(self):
        for s in self.doc.sections:
            s.top_margin = Inches(1.0)
            s.bottom_margin = Inches(1.0)
            s.left_margin = Inches(1.0)
            s.right_margin = Inches(1.0)

    def _add_header(self):
        # Course metadata
        p_course = self.doc.add_paragraph()
        p_course.paragraph_format.space_before = Pt(0)
        p_course.paragraph_format.space_after = Pt(2)
        r_course = p_course.add_run(f"Course Code: {self.course_code}")
        r_course.font.bold = True
        r_course.font.size = Pt(11)
        r_course.font.color.rgb = CHARCOAL_RGB

        # Document Title
        p_title = self.doc.add_paragraph()
        p_title.paragraph_format.space_before = Pt(2)
        p_title.paragraph_format.space_after = Pt(4)
        r_title = p_title.add_run(self.title)
        r_title.font.bold = True
        r_title.font.size = Pt(16)
        r_title.font.color.rgb = CHARCOAL_RGB

        # Student & Date
        p_meta = self.doc.add_paragraph()
        p_meta.paragraph_format.space_after = Pt(8)
        r_s_lbl = p_meta.add_run("Student: ")
        r_s_lbl.font.italic = True
        r_s_lbl.font.color.rgb = MUTED_RGB
        r_s_val = p_meta.add_run(f"{self.student_name} | ")
        r_s_val.font.bold = True
        r_s_val.font.color.rgb = CHARCOAL_RGB
        r_d_lbl = p_meta.add_run("Date: ")
        r_d_lbl.font.italic = True
        r_d_lbl.font.color.rgb = MUTED_RGB
        r_d_val = p_meta.add_run(self.date_str)
        r_d_val.font.color.rgb = CHARCOAL_RGB

        # Subtle Header Divider: 1px accent #E2B4BD
        p_div = self.doc.add_paragraph()
        p_div.paragraph_format.space_after = Pt(16)
        pPr = p_div._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="1" w:color="{ACCENT_HEX}"/></w:pBdr>')
        pPr.append(pBdr)

    def add_heading(self, text, level=1):
        sizes = {1: Pt(14), 2: Pt(12), 3: Pt(11)}
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = sizes.get(level, Pt(11))
        r.font.color.rgb = CHARCOAL_RGB
        return p

    def add_paragraph(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(text)
        r.font.size = Pt(10.5)
        r.font.color.rgb = CHARCOAL_RGB
        return p

    def add_callout(self, label, text):
        """Adds a critical callout with a 2px-3px left accent border (#E2B4BD)."""
        tbl = self.doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.5)

        cell = tbl.cell(0, 0)
        set_cell_margins(cell, top=100, bottom=100, left=180, right=140)
        # Left border: single, sz 18 (2.25pt), #E2B4BD
        set_cell_borders(cell, left=('single', '18', ACCENT_HEX))

        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r_lbl = p.add_run(f"{label}: ")
        r_lbl.font.bold = True
        r_lbl.font.size = Pt(10)
        r_lbl.font.color.rgb = CHARCOAL_RGB

        r_txt = p.add_run(text)
        r_txt.font.size = Pt(10)
        r_txt.font.color.rgb = CHARCOAL_RGB

        # Spacing after callout table
        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(8)

    def add_minimal_table(self, headers, rows):
        """Creates a table without solid color fills or alternating stripes."""
        tbl = self.doc.add_table(rows=len(rows) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = True

        # Header Row
        for col_idx, h_text in enumerate(headers):
            cell = tbl.cell(0, col_idx)
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            # Bottom border 12 (1.5pt) in charcoal
            set_cell_borders(cell, bottom=('single', '12', CHARCOAL_HEX))
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(h_text)
            r.bold = True
            r.font.size = Pt(9.5)
            r.font.color.rgb = CHARCOAL_RGB

        # Data Rows
        for r_idx, row_data in enumerate(rows):
            is_last = (r_idx == len(rows) - 1)
            b_border = ('single', '8', 'D0D0D0') if is_last else ('single', '4', 'EEEEEE')
            for col_idx, val in enumerate(row_data):
                cell = tbl.cell(r_idx + 1, col_idx)
                set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
                set_cell_borders(cell, bottom=b_border)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(str(val))
                r.font.size = Pt(9.5)
                r.font.color.rgb = CHARCOAL_RGB

        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(10)

    def save(self, filepath):
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        self.doc.save(filepath)
        print(f"[SUCCESS] Academic DOCX saved: {filepath}")
