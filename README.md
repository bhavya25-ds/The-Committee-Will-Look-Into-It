# The Committee Will Look Into It

> *India does not lack laws, courts, or institutions. It has all of them.*
> *Yet the system delivers the same answer every time: nothing.*

A data investigation that uses the government's own publicly available records to map exactly where, when, and under whose watch institutional accountability disappears in India.

This is not an opinion. This is a receipt.

---

## What This Investigation Covers

| Module | Focus | Primary Data Sources |
|--------|-------|---------------------|
| `01_Exam_Frauds` | Merit stolen by exam fraud — NTA irregularities, paper leaks, and the students who paid the price | NTA notices, affidavits, court orders |
| `02_Gender_Injustice` | Cases that collapsed before reaching trial — attrition rates, conviction gaps, pendency | NCRB Crime in India reports |
| `03_MP_Performance` | Representatives who showed up only on paper — attendance, debates, questions asked | ADR MP profiles, Lok Sabha records |
| `04_Suppression_of_Dissent` | Protests lathi-charged and petitions left unheard — Section 144 impositions, UAPA usage | MHA data, court filings, RTI records |
| `05_Corruption_Electoral_Bonds` | The money trail behind policy decisions | Electoral bond disclosures (SBI/ECI), ADR analysis |

---

## Methodology

Every claim in this investigation is derived from **government-published or court-published data**:

- **NCRB** — National Crime Records Bureau, *Crime in India* annual reports
- **NTA** — National Testing Agency public notices and official communications
- **ADR** — Association for Democratic Reforms MP/MLA affidavit database
- **Supreme Court / High Court** — Case timelines via eCourts and NJDG
- **ECI / SBI** — Electoral bond purchase and redemption data released under Supreme Court order
- **Section 144 records** — District magistrate orders obtained via RTI and state government portals

Data is cleaned, structured, and versioned in each module. All raw source files are preserved as-downloaded.

---

## Repository Structure

```
the-committee-will-look-into-it/
│
├── 01_Exam_Frauds/
│   ├── data/          # Raw + cleaned datasets
│   ├── notebooks/     # Analysis and findings
│   └── README.md      # Module-level methodology notes
│
├── 02_Gender_Injustice/
├── 03_MP_Performance/
├── 04_Suppression_of_Dissent/
├── 05_Corruption_Electoral_Bonds/
│
├── utility.py         # Shared data cleaning and analysis helpers
└── README.md
```

---

## How to Use This Repo

```bash
git clone https://github.com/bhavya25-ds/the-committee-will-look-into-it.git
cd the-committee-will-look-into-it
pip install -r requirements.txt  # coming soon
```

Each module folder contains its own README with source citations, cleaning decisions, and key findings.

---

## Status

| Module | Data Collected | Analysis | Published |
|--------|:--------------:|:--------:|:---------:|
| Exam Frauds | 🔄 | ⬜ | ⬜ |
| Gender Injustice | 🔄 | ⬜ | ⬜ |
| MP Performance | 🔄 | ⬜ | ⬜ |
| Suppression of Dissent | 🔄 | ⬜ | ⬜ |
| Electoral Bonds | 🔄 | ⬜ | ⬜ |

---

## A Note on Intent

This project does not editorialize. The data speaks. Every chart, table, and timeline is reproducible from the source files included in this repository. If a number is wrong, open an issue with a citation. That is the standard this investigation holds itself to — the same standard it asks of the institutions it examines.

---

*Built by [@bhavya25-ds](https://github.com/bhavya25-ds)*
