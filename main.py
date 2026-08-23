from agents.extraction_agent import extraction_agent
from agents.relevance_agent import relevance_agent
from agents.impact_agent import impact_agent
from agents.judge_agent import judge_agent

regulation_text = """
The Ministry of Agriculture has introduced a new regulation
requiring farmers to maintain records of fertilizer usage
for agricultural land.
"""
# -----------------------------
# Agent 1: Extraction
# -----------------------------


regulation = extraction_agent(regulation_text)

print("\n==============================")
print("AGENT 1 - EXTRACTION")
print("==============================")

print("\n--- EXTRACTION RESULT ---")
print(regulation)

# -----------------------------
# Agent 2: Relevance
# -----------------------------

relevance = relevance_agent(regulation)

print("\n==============================")
print("AGENT 2 - RELEVANCE")
print("==============================")

print(relevance)

# --------------------------------
# Agent 3 - Impact Analysis
# --------------------------------

if relevance.relevant:
    impact = impact_agent(regulation,relevance)

    print("\n==============================")
    print("AGENT 3 - IMPACT ANALYSIS")
    print("==============================")

    print(impact)
# else:
#
#     print("\nRegulation is not relevant.")
#     print("Impact analysis skipped.")


    # --------------------------------
    # Agent 4 - Judge
    # --------------------------------


    judge=judge_agent(regulation,relevance,impact)

    print("\n==============================")
    print("AGENT 4 - JUDGE")
    print("==============================")

    print(judge)

    # --------------------------------
    # Final Decision
    # --------------------------------

    print("\n==============================")
    print("FINAL DECISION")
    print("==============================")

    if judge.approved:
        print("APPROVED")
        print("Recommendation: ", judge.recommendation)
    else:
        print("REJECTED")
        print("Issues:")
        for issue in judge.issues:
            print("-",issue)
else:
    print("\nRegulation is not relevant.")
    print("Impact analysis skipped.")
