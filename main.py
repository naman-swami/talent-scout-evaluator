import argparse
import json
import os
from auditors.adverse_impact_checker import CandidateEvaluatorEngine

def main():
    parser = argparse.ArgumentParser(description="Talent Scout Evaluator CLI")
    parser.add_argument("--demo", action="store_true", help="Evaluate sample candidate pool")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "candidates", "sample_applicant_pool.json")

    if args.demo:
        with open(data_file, "r") as f:
            pool = json.load(f)
        print("=== TALENT SCOUT CANDIDATE EVALUATION REPORT ===\n")
        audited_cohort = []
        for c in pool:
            res = CandidateEvaluatorEngine.score_candidate(c["technical_score"], c["leadership_score"], c["system_design"])
            audited_cohort.append({"group": c["group"], "passed": res["pass_interview_gate"]})
            print(f"Candidate: {c['name']} (Group: {c['group']})")
            print(f"  Composite Score: {res['composite_score']} / 100 | Tier: {res['hiring_tier']}")
            print(f"  Recommendation: {'PASS' if res['pass_interview_gate'] else 'FAIL'}")
            print("-" * 50)

        eeoc_audit = CandidateEvaluatorEngine.audit_adverse_impact(audited_cohort)
        print("=== EEOC ADVERSE IMPACT AUDIT ===")
        print(f"Majority Selection Rate: {eeoc_audit['majority_selection_rate']*100:.1f}%")
        print(f"Protected Selection Rate: {eeoc_audit['protected_selection_rate']*100:.1f}%")
        print(f"Adverse Impact Ratio: {eeoc_audit['adverse_impact_ratio']} (Threshold: >= 0.80)")
        print(f"Status: {eeoc_audit['compliance_status']}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
