"""
Talent Scout Candidate Scoring & EEOC 4/5ths Rule Adverse Impact Auditor
Calculates weighted competency ratings and audits hiring pass-rate ratios across demographic groups.
"""
from typing import List, Dict, Any

class CandidateEvaluatorEngine:
    @staticmethod
    def score_candidate(technical: float, leadership: float, system_design: float) -> Dict[str, Any]:
        # Weighted composite score: 45% Tech, 35% System Design, 20% Leadership
        composite = round(0.45 * technical + 0.35 * system_design + 0.20 * leadership, 1)
        passed = composite >= 80.0
        return {
            "composite_score": composite,
            "pass_interview_gate": passed,
            "hiring_tier": "STRONG_HIRE" if composite >= 88.0 else "HIRE" if passed else "NO_HIRE"
        }

    @staticmethod
    def audit_adverse_impact(pool_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        majority = [c for c in pool_results if c.get("group") == "MAJORITY"]
        protected = [c for c in pool_results if c.get("group") == "PROTECTED"]

        maj_pass_rate = sum(1 for c in majority if c.get("passed")) / max(1, len(majority))
        prot_pass_rate = sum(1 for c in protected if c.get("passed")) / max(1, len(protected))

        impact_ratio = round(prot_pass_rate / max(0.01, maj_pass_rate), 2)
        has_adverse_impact = impact_ratio < 0.80 # EEOC 4/5ths Rule (80%)

        return {
            "majority_selection_rate": round(maj_pass_rate, 2),
            "protected_selection_rate": round(prot_pass_rate, 2),
            "adverse_impact_ratio": impact_ratio,
            "eeoc_compliant": not has_adverse_impact,
            "compliance_status": "COMPLIANT_WITH_EEOC_4_5THS" if not has_adverse_impact else "POTENTIAL_DISPARATE_IMPACT"
        }
