
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the scorer agent
gcp_product_extractor_agent = LlmAgent(
    name="gcp_product_extractor",
    model=GEMINI_MODEL,
    instruction="""You are a GCP Cloud Architect based off the use case, understand the list of Google Cloud Products that maybe needed for the solution.

    Use the "use case" field in {extracted_sa} and generate appropriate GCP products, use the google_search tool. 


    Extract ONLY the values of the GCP product in JSON format in product_json output. 
    """,
    description="GCP Archicect for extracting product names from use case",
    output_key="product_json",
    tools=[google_search]
)
