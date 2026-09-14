# The Committee Will Look Into It
> *India does not lack laws, courts, or institutions. It has all of them.*
> *Yet the system delivers the same answer every time: nothing.*

A data investigation that uses the government's own publicly available records to map exactly where, when, and under whose watch institutional accountability disappears in India.

This is not an opinion. This is a receipt.

---

## What This Investigation Covers

| Module | Focus | Primary Data Sources |
|--------|-------|---------------------|
| `01_Exam_Frauds` | Merit stolen by exam fraud — paper leaks, impersonation rackets, and the aspirants who paid the price | Hand-compiled incident dataset (2004–2026) sourced from NCRB, court records, NTA notices, and press archives |
| `02_Gender_Injustice` | Crimes against women over two decades — trends, conviction gaps, metropolitan hotspots | NCRB *Crime in India* annual reports (2001–2023), state-wise and metro-level breakdowns |
| `03_MP_Performance` | Representatives who showed up only on paper — attendance, debates, questions asked | ADR MP profiles, Lok Sabha records |
| `04_Suppression_of_Dissent` | Protests lathi-charged and communications cut — Section 144 impositions and internet shutdowns | RTI-sourced Section 144 report (district-level, Delhi), internet shutdown tracker data |
| `05_Corruption_Electoral_Bonds` | The money trail behind policy decisions | Electoral bond disclosures (SBI/ECI), ADR analysis |

---

## Methodology

Every claim in this investigation is derived from **government-published, court-published, or RTI-sourced data**:

- **NCRB** — National Crime Records Bureau, *Crime in India* annual reports
- **NTA / NEET records** — National Testing Agency public notices and official communications
- **ADR** — Association for Democratic Reforms MP/MLA affidavit database
- **Supreme Court / High Court** — Case timelines via eCourts and NJDG
- **ECI / SBI** — Electoral bond purchase and redemption data released under Supreme Court order
- **Section 144 & internet shutdown records** — District magistrate orders obtained via RTI and civil-liberties tracking databases

Data is cleaned, structured, and versioned in each module. All raw source files are preserved as-downloaded.

---

## Repository Structure

```
the-committee-will-look-into-it/
│
├── 01_Exam_Frauds/
│   ├── 01_EDA.ipynb
│   ├── 02_Cleaning.ipynb
│   ├── 03_Analysis.ipynb
│   ├── paper_leaks.csv          # Raw incident dataset (110 incidents, 2004–2026)
│   ├── paper_leaks_cleaned.csv  # Cleaned version
│   └── charts/                  # Exported visualisations
│
├── 02_Gender_Injustice/
│   ├── 01_EDA.ipynb
│   ├── 02_Cleaning.ipynb
│   ├── 03_Analysis.ipynb        # In progress
│   └── data/
│       ├── 01 Crime against Women (2001-2022).csv
│       ├── 02 combined_crime_against_women_full.csv
│       ├── 03 NCRB_CII_2023_Table_3A.8_0.csv
│       ├── 04 crimes-against-women-in-metros-2022.csv
│       ├── 05 Crime against Women During 2023.xlsx
│       ├── 06 Crimes against Women in 53 Metropolitan Cities During 2023.xlsx
│       ├── 07 Rape 2019.csv
│       └── cleaned/             # file1.csv – file7.csv
│
├── 03_MP_Performance/
│
├── 04_Suppression_of_Dissent/
│   ├── 01_EDA.ipynb
│   ├── 02_Analysis.ipynb
│   ├── 03_Observations.md
│   ├── charts/                  # Exported visualisations
│   └── data/
│       ├── 01_144-Report-release-version.pdf   # RTI-sourced Section 144 orders (Delhi, district-level)
│       ├── 02_Internet shutdown.docx            # Internet shutdown log
│       ├── file1.csv            # Section 144 order counts by Delhi district
│       ├── file2.csv            # Internet shutdown events by state/district/date
│       ├── df_combined.csv
│       └── df_cleaned.csv
│
├── 05_Corruption_Electoral_Bonds/
│
├── utility.py                   # Shared data loading and analysis helpers
└── README.md
```

---

## How to Use This Repo

```bash
git clone https://github.com/bhavya25-ds/the-committee-will-look-into-it.git
cd the-committee-will-look-into-it
pip install -r requirements.txt  # coming soon
```

Each module folder contains its own notebooks with source citations, cleaning decisions, and key findings.

---

## Status

| Module | Data Collected | Analysis | Observation |
|--------|:--------------:|:--------:|:---------:|
| Exam Frauds | ✅ | ✅ | ✅ |
| Gender Injustice | ✅ | ✅ | ✅ |
| MP Performance | ✅ | ⬜ | ⬜ |
| Suppression of Dissent | ✅ | ✅ | ✅ |
| Electoral Bonds | ✅ | ⬜ | ⬜ |

---

## A Note on Intent

This project does not editorialize. The data speaks. Every chart, table, and timeline is reproducible from the source files included in this repository. If a number is wrong, open an issue with a citation. That is the standard this investigation holds itself to — the same standard it asks of the institutions it examines.

---

*Built by [@bhavya25-ds](https://github.com/bhavya25-ds)*
