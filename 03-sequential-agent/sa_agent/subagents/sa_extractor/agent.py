
from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the validator agent
sa_extractor_agent = LlmAgent(
    name="sa_extractor_agent",
    model=GEMINI_MODEL,
    instruction="""You are a extracted agent for SA. Extract the following fields in a structured JSON:

    1. Use case
    2. Customer name 
    3. Use Case
    
    
    """,
    description="Validates an SA",
    output_key="extracted_sa")
