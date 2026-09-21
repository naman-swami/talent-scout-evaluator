import os
import pytest
from auditors.adverse_impact_checker import CandidateEvaluatorEngine

def test_candidate_scoring_weights():
    res = CandidateEvaluatorEngine.score_candidate(technical=100.0, leadership=100.0, system_design=100.0)
    assert res["composite_score"] == 100.0
    assert res["pass_interview_gate"]
    assert res["hiring_tier"] == "STRONG_HIRE"

def test_eeoc_fairness_audit():
    cohort = [
        {"group": "MAJORITY", "passed": True},
        {"group": "PROTECTED", "passed": True}
    ]
    res = CandidateEvaluatorEngine.audit_adverse_impact(cohort)
    assert res["eeoc_compliant"]
    assert res["adverse_impact_ratio"] == 1.0
