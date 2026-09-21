# Talent Scout Candidate Evaluator & EEOC Bias Auditor

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![HRTech](https://img.shields.io/badge/Domain-Talent_Assessment_EEOC-darkblue.svg)](docs/eeoc_uniform_guidelines.md)
[![Standard](https://img.shields.io/badge/Standard-EEOC_4%2F5ths_Rule-green.svg)](docs/eeoc_uniform_guidelines.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An enterprise technical candidate scoring and algorithmic fairness engine evaluating interview rubrics while auditing hiring cohorts against the EEOC 4/5ths rule for adverse impact.

```
                    ┌─────────────────────────┐
                    │ Applicant Competencies  │
                    │ (Tech, Design, Lead)    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ auditors/adverse_impact │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │ Composite Score     │         │ EEOC 4/5ths Audit   │
      │ 45% Tech, 35% Sys   │         │ (Ratio >= 80%)      │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Hiring Recommendation   │
                    │ (HIRE / DISPARATE_WARN) │
                    └─────────────────────────┘
```

## Features

- **Weighted Competency Scoring**: Evaluates engineering architecture, coding proficiency, and technical communication.
- **EEOC 4/5ths Adverse Impact Audit**: Continuously checks candidate cohort pass rates to eliminate systemic demographic bias.
- **Candidate Pool Fixtures**: Packaged with representative applicant pool data.

## Directory Structure

```
talent-scout-evaluator/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint HR fairness provenance
├── auditors/
│   └── adverse_impact_checker.py    # Composite scoring and EEOC bias checker
├── fixtures/
│   └── candidates/
│       └── sample_applicant_pool.json # Benchmark candidate pool
├── docs/
│   └── eeoc_uniform_guidelines.md   # Federal regulatory reference
├── tests/
│   └── test_agent.py                # Talent evaluation test suite
├── main.py                          # Talent assessment CLI
└── requirements.txt
```

## Quick Start

```bash
# Run candidate assessment tests
pytest tests/ -v

# Audit sample applicant pool
python main.py --demo
```
