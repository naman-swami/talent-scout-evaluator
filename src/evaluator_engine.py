"""
Talent Scout Evaluator Engine
Objective technical interview rubric scoring with bias mitigation and leveling alignment.
"""
from typing import Dict, Any, List

class TalentScoutEngine:
    def __init__(self):
        self.bias_phrases = ["culture fit", "too academic", "aggressive", "rockstar", "pedigree", "gut feeling"]

    def audit_feedback(self, feedback_notes: str, rubric_scores: Dict[str, int]) -> Dict[str, Any]:
        notes_lower = feedback_notes.lower()
        found_biases = [p for p in self.bias_phrases if p in notes_lower]

        scores = list(rubric_scores.values())
        avg_score = round(sum(scores) / len(scores), 2) if scores else 0.0

        recommendation = "HIRE" if avg_score >= 4.0 and not found_biases else "REVISE_NOTES_EVIDENCE_BASED" if found_biases else "NO_HIRE"

        return {
            "average_rubric_score": avg_score,
            "detected_bias_phrases": found_biases,
            "has_bias_flags": len(found_biases) > 0,
            "hiring_verdict": recommendation,
            "confidence_score": 0.95
        }
