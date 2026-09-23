**Course Code: CS301 | Database Systems**

**Activity 04: Relational Schema Normalization**

*Student:* Godwyn Neri | *Date:* September 24, 2026

---

#### 1. Objectives

* Identify functional dependencies within an unnormalized data set.
* Convert a flat relation into Third Normal Form (3NF).
* Verify referential integrity constraints across newly decomposed relations.

> **Key Constraint:** Foreign keys must explicitly reflect cascading delete rules defined in Section 3.2.

---

#### 2. Relational Decompositions & Normalization State

The table below summarizes the normalization progression for each decomposed entity:

| Table Name | Primary Key | Normal Form | Status |
| --- | --- | --- | --- |
| `tbl_students` | `student_id` | 3NF | [VERIFIED] |
| `tbl_courses` | `course_id` | 3NF | [VERIFIED] |
| `tbl_enrollments` | `enrollment_id` | 3NF | [VERIFIED] |
| `tbl_instructors` | `instructor_id` | 3NF | [PENDING] |

---

#### 3. Verification & Integrity Summary

All transitively dependent attributes (`department_name`, `office_location`) have been decoupled from the primary entity key into lookup relations, thereby eliminating update, insertion, and deletion anomalies.
