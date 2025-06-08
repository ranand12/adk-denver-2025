

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"


sa_composer_agent = LlmAgent(
    name="sa_composer_agent",
    model=GEMINI_MODEL,
    instruction="""You are a composer of the final SA.

    You compose a SA output using the {product_json} and {extracted_sa} in a human readable format like this : 

    This is SA - Version 2.1 

    Customer name : Customer name from {extracted_sa}
    Use case : Use case from {extracted_sa}
    Quote : Quote from {extracted_sa}
    Product list : Conver the JSON to a neatly formatted list {product_json} 
    SA Markup Quote : Add a 30% markup to the Quote from {extracted_sa}

    Approvals needed by : Management

    """,
    description="SA composer based off values extracted",
    output_key="sa_composer",
)
