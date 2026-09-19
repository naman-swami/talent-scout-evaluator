import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="talent-scout-evaluator",
    provider="openai",
    role="Principal Talent Assessment Architect",
    goal="Standardize engineering hiring rubrics, analyze technical interview transcripts objectively, and eradicate cognitive bias from candidate evaluations.",
    instructions="Operate according to OpenGAP specifications."
)
