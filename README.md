# STI College Academic Workspace

[![Student](https://img.shields.io/badge/Student-Godwyn%20Neri-blue.svg)](#)
[![Institution](https://img.shields.io/badge/Institution-STI%20College-yellow.svg)](#)
[![AI Integration](https://img.shields.io/badge/AI%20Assisted-Antigravity%20%2F%20Gemini-green.svg)](#)
[![Global MCP](https://img.shields.io/badge/Brave%20Automation-Active%20Global-orange.svg)](#)

Central repository for all **STI College** coursework, laboratory exercises, performance tasks, handouts, syllabi, and study materials.

---

## 📚 Enrolled Subjects & Coursework

| Subject Directory | Full Course Name | Focus Area |
| :--- | :--- | :--- |
| [`courses/Computer_Graphics_Programming/`](file:///C:/Users/Godwyn/Documents/Projects/STI-College/courses/Computer_Graphics_Programming) | Computer Graphics Programming | 3D Wireframe rendering, geometry, projection matrices |
| [`courses/Game_Development/`](file:///C:/Users/Godwyn/Documents/Projects/STI-College/courses/Game_Development) | Game Development | Game engines, physics, rendering loops, scripts |
| [`courses/IT_Service_Management/`](file:///C:/Users/Godwyn/Documents/Projects/STI-College/courses/IT_Service_Management) | IT Service Management | ITIL v4 frameworks, CSI, Service Operations, SLAs |
| [`courses/Information_Assurance_and_Security/`](file:///C:/Users/Godwyn/Documents/Projects/STI-College/courses/Information_Assurance_and_Security) | Information Assurance & Security | AWS Cloud, IAM policies, VPC security, encryption |
| [`courses/Network_Technology_2/`](file:///C:/Users/Godwyn/Documents/Projects/STI-College/courses/Network_Technology_2) | Network Technology 2 | Cloud architecture, VPC peering, packet capture, subnets |
| [`courses/IT_Capstone_Project_2/`](file:///C:/Users/Godwyn/Documents/Projects/STI-College/courses/IT_Capstone_Project_2) | IT Capstone Project 2 | Senior capstone design, documentation, implementation |
| [`courses/Euthenics_2/`](file:///C:/Users/Godwyn/Documents/Projects/STI-College/courses/Euthenics_2) | Euthenics 2 | Values education, leadership, professional ethics |

---

## 🏛️ Standard Module Directory Structure

Every academic module, exercise, and assignment follows this clean layout:

```
courses/<Subject_Name>/
├── handouts/              # Downloaded lecture slides, PDFs, notes
├── syllabi/               # Course syllabi, grading policies
└── assignments/
    ├── midterm/
    │   └── <Module_Name>/ # e.g., 03_Activity_1, 03_Laboratory_Exercise_1
    │       ├── materials/ # Source PDF handout, prompts, teacher diagrams
    │       ├── src/       # Executable source code (Python, C++, JS, Draw.io)
    │       ├── answer.md  # Primary human-grade submission report
    │       └── .tmp/      # Temporary extracted text (gitignored)
    └── finals/
```

---

## ⚡ Autonomous Student Skills (`.agents/skills/`)

| Skill | Purpose | Trigger / Usage |
| :--- | :--- | :--- |
| **`academic-assignment`** | Solves assignments with strict prompt compliance and zero artificial fluff | Run whenever completing lab activities or performance tasks |
| **`academic-pdf`** | Generates clean, publication-grade monochrome PDF & Word deliverables | Converts `answer.md` into `answer.pdf` or `.docx` ready for submission |
| **`sti-elms`** | Fast batch downloader for course handouts, syllabi, and assignment PDFs | Uses global `brave-control` MCP to scrape/download materials automatically |

---

## 🌐 Browser Automation & STI ELMS

This workspace leverages the global **`brave-control`** MCP server to connect Antigravity directly to your running Brave browser:
- Download handouts and assignment sheets directly into `materials/`.
- Check deadlines and view announcements without manual navigation.
- No local browser infrastructure files needed—it connects directly via `~/.gemini/config/mcp_config.json`.
