import json
import argparse
from src.evaluator_engine import TalentScoutEngine

def main():
    parser = argparse.ArgumentParser(description="Talent Scout Evaluator CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated interview bias & rubric audit")
    args = parser.parse_args()

    engine = TalentScoutEngine()
    feedback = "Candidate solved distributed consensus cleanly, but gut feeling was that culture fit was slightly off."
    rubrics = {"system_design": 5, "algorithms": 4, "communication": 4, "problem_solving": 5}

    report = engine.audit_feedback(feedback, rubrics)
    print("="*60)
    print(" TALENTSCOUT OBJECTIVE COMPETENCY AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
