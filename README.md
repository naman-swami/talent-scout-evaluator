# Talent Scout Objective Evaluator & DEI Auditor

> **Unbiased Structured Competency Scoring & EEOC Adverse Impact Auditor**  
> Enforcing the Title VII Four-Fifths (80%) Rule to Eliminate Demographic Hiring Disparities.

---

### The EEOC Four-Fifths (80%) Rule

Under the Equal Employment Opportunity Commission (EEOC) Uniform Guidelines on Employee Selection Procedures:

$$\text{Impact Ratio} = \frac{\text{Selection Rate of Protected Group}}{\text{Selection Rate of Highest Group}} \ge 0.80$$

An adverse impact ratio below $0.80$ ($80\%$) establishes prima facie statistical evidence of discriminatory selection bias, triggering mandatory rubrics review.

---

### Competency-Based Scoring Rubrics

Candidates are evaluated solely through structured behavioral and technical competencies:

| Evaluation Trait | Scoring Rubric Focus | Weight |
| :--- | :--- | :--- |
| **Algorithmic Mastery** | Code efficiency, time complexity, and edge case handling | 35% |
| **System Architecture** | Scalability, state management, and failure recovery design | 30% |
| **Collaborative Problem Solving** | Clear technical communication and receptive code review | 20% |
| **Operational Rigor** | Observability, automated testing, and CI/CD discipline | 15% |

---

### Candidate Pool Audit CLI

```bash
# Audit sample applicant cohort for adverse impact
python evaluate.py --demo

# Run EEOC compliance unit test suite
pytest tests/ -v
```

Organizational diversity guidelines, structured interview rubrics, and adverse impact mitigations are detailed in [DEI_SELECTION_POLICY.md](DEI_SELECTION_POLICY.md).
