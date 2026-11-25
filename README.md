# Replication Package: Infrastructure-Induced Technical Debt in ML/DL Systems

This repository contains the complete replication package for the systematic literature review:

**"Infrastructure-Induced Technical Debt in Machine Learning and Deep Learning Systems: A Systematic Literature Review Protocol"**

\---

## Authors \& Affiliations

* **Eesha Naveed** (Roll No: 26015998-001) — Primary Reviewer (Data Extraction \& Analysis)
* **Hafsa Shamriz** (Roll No: 26015998-010) — Secondary Reviewer (Paper Screening \& Verification)
* **Domain:** Software Engineering / MLOps / AI Systems

\---

## Repository Structure

```text
├── Activity Sheet Search, Screen and Snowball.docx   # Database search strings, search log, and SLR protocol
├── calculate\\\_kappa.py                                # Python script to compute Observed Agreement \\\& Cohen's Kappa
├── Test - data Extraction.csv                        # Extracted data for 33 primary studies across taxonomy facets
├── Test - Partner 1.csv                              # Screening decisions recorded by Reviewer 1 (Eesha Naveed)
├── Test - Partner 2.csv                              # Screening decisions recorded by Reviewer 2 (Hafsa Shamriz)
├── Test - Screening Sheet.csv                        # 106 unique papers screened independently by both reviewers
├── Test - SnowBalling.csv                            # Tracking 12 seed papers + 21 snowballing 
└── README.md                                         # Replication package documentation
```

\---

## Systematic Review Summary

### Search \& Database Results (Oct 19, 2026)

* **IEEE Xplore:** 7 records
* **ACM Digital Library:** 3 records
* **Google Scholar:** 93 records
* **arXiv:** 3 records
* **Total Records Retrieved:** 106 records 

### PRISMA Selection Funnel

1. **Initial Records:** 106
2. **Unique Records (After Duplicates):** 106
3. **Title \& Abstract Screening:** 23 candidate papers (83 excluded)
4. **Full-Text Screening (Seed Set):** 12 seed papers (11 excluded)
5. **Snowballing \& Expansion:** +21 papers (16 backward, 5 forward)
6. **Final Primary Corpus:** **33 papers**

\---

## Inter-Rater Reliability (Cohen's Kappa)

Both reviewers independently screened all 106 unique papers against inclusion (I1–I4) and exclusion (E1–E4) criteria.

* **Sample Size ($N$):** 106 papers
* **Dual Inclusions ($a$):** 21 papers
* **Disagreements ($b, c$):** 5 papers (3 Eesha Inc / Hafsa Exc; 2 Eesha Exc / Hafsa Inc) — *resolved via consensus*
* **Dual Exclusions ($d$):** 80 papers
* **Observed Agreement ($P\_o$):** 95.28% ($\\frac{101}{106}$)
* **Chance Agreement ($P\_e$):** 65.49%
* **Cohen's Kappa ($\\kappa$):** **0.8633** (*"Almost Perfect Agreement"* per Landis \& Koch, 1977)

\---

## Classification Scheme \& Taxonomy

Extracted studies were categorized across three primary facets:

1. **Technical Debt Focus (Topic):** Data Debt; Model Debt; Code/SATD Debt; Architectural Debt; API/Compatibility Debt; Infrastructure Debt *(Adapted from Sculley et al., 2015 \& Bogner et al., 2021)*.
2. **Evolution Trigger:** API Deprecation; Framework Migration; Hardware/GPU Shifts; Model Memory Lag; Pipeline Reconfiguration *(Inductively derived via keywording)*.
3. **Research Type:** Empirical Study; Tool/Framework Proposal; Systematic Review; Exploratory Case Study *(Adapted from Wieringa et al., 2006)*.

\---

## Usage Instructions

To reproduce the inter-rater agreement statistics and Kappa calculations:

### Run Python Script

```bash
python3 calculate\\\_kappa.py
```

## File Details

|File Name|Description|
|-|-|
|`Activity Sheet Search, Screen and Snowball.docx`|Full search protocol, Boolean strings, and screening log details.|
|`calculate\\\_kappa.py`|Python script calculating Observed Agreement (95.28%) and Cohen's Kappa ($\\kappa = 0.8633$).|
|`Test - data Extraction.csv`|Structured data extraction across all 44 primary studies.|
|`Test - Partner 1.csv`|Initial screening decisions by Reviewer 1 (Eesha Naveed).|
|`Test - Partner 2.csv`|Initial screening decisions by Reviewer 2 (Hafsa Shamriz).|
|`Test - Screening Sheet.csv`|Joint screening matrix for all 106 unique records with disagreement resolutions.|
|`Test - SnowBalling.csv`|Tracking sheet for seed set, backward snowballing, forward snowballing, and expansion papers.|
|`README.md`|Complete replication package documentation and metadata.|

\---

## License \& Citation

This replication package is made available for academic and research evaluation purposes.

