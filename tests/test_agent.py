import pytest
from src.evaluator_engine import TalentScoutEngine

def test_bias_phrase_flagging():
    engine = TalentScoutEngine()
    notes = "Good coding, but felt culture fit was off based on gut feeling."
    res = engine.audit_feedback(notes, {"coding": 4, "design": 4})
    assert res["has_bias_flags"] is True
    assert "culture fit" in res["detected_bias_phrases"]
    assert res["hiring_verdict"] == "REVISE_NOTES_EVIDENCE_BASED"

def test_objective_high_score():
    engine = TalentScoutEngine()
    notes = "Candidate demonstrated solid grasp of Paxos quorum and thread synchronization."
    res = engine.audit_feedback(notes, {"coding": 5, "design": 5})
    assert res["has_bias_flags"] is False
    assert res["hiring_verdict"] == "HIRE"
