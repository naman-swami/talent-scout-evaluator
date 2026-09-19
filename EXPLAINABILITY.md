# Explainability — talent-scout-evaluator

## Decision Reasoning
TalentScout evaluates talent by decoupling objective problem-solving evidence from subjective commentary, mapping demonstrated accomplishments directly to validated role rubrics.

## Data Sources and Inputs Used
SFIA competency matrices, structured interview rubrics, EEOC compliance guidelines, and empirical hiring outcome datasets.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, talent-scout-evaluator assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, talent-scout-evaluator will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, talent-scout-evaluator explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
talent-scout-evaluator actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Hiring Decisions: Does not make final hiring/firing decisions; all recommendations are advisory to human hiring committees.
- Cultural Conformity: Explicitly ignores non-job-related subjective personal preferences.
- Credentialism: Evaluates demonstrated skill competencies rather than alma mater prestige.
- Compensation: Does not negotiate equity grants or compensation packages.

## Uncertainty Quantification Approach
When candidate performance in an interview fluctuates across disparate interviewers, TalentScout flags the high variance score, highlights specific contradicting signals, and recommends an objective tie-breaker session.
