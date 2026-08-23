from agents.extraction_agent import extraction_agent


regulation_text = """
RBI has issued a new regulation requiring financial
institutions to retain customer transaction records
for a minimum period of seven years.

The regulation becomes effective from January 1, 2027.
"""


regulation = extraction_agent(regulation_text)

print("\n--- EXTRACTION RESULT ---")
print(regulation)

print("\n--- REGULATION NAME ---")
print(regulation.regulation_name)

print("\n--- EFFECTIVE DATE ---")
print(regulation.effective_date)

print("\n--- REQUIREMENTS ---")
for requirement in regulation.requirements:
    print("-", requirement)

print("\n--- AFFECTED ENTITIES ---")
for entity in regulation.affected_entities:
    print("-", entity)