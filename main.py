from agents.extraction_agent import extraction_agent
from agents.relevance_agent import relevance_agent
from agents.impact_agent import impact_agent
from agents.judge_agent import judge_agent
from ingestion.pdf_loader import extract_text_from_pdf

# regulation_text = """
# RBI has issued a new regulation requiring financial
# institutions and technology service providers that
# process customer transaction data to retain transaction
# records for a minimum period of seven years.
#
# Organizations must ensure that customer transaction data
# is securely stored and available for regulatory audits.
#
# The regulation becomes effective from January 1, 2027.
#
# """


# --------------------------------
# Load PDF
# --------------------------------

pdf_path = "data/regulations/rbi_regulation.pdf"

regulation_text = extract_text_from_pdf(pdf_path)


print("\n==============================")
print("PDF LOADED")
print("==============================")

print(f"Characters extracted: {len(regulation_text)}")

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
