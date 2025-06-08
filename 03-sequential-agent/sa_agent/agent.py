
from google.adk.agents import SequentialAgent

from .subagents.gcp_product_extractor import gcp_product_extractor_agent
from .subagents.sa_extractor import sa_extractor_agent
from .subagents.sa_composer import sa_composer_agent

# Create the sequential agent with minimal callback
root_agent = SequentialAgent(
    name="sa_helper_agent",
    sub_agents=[sa_extractor_agent,gcp_product_extractor_agent,sa_composer_agent],
    description="A pipeline that extracts values for SA, gets relevant GCP products and composed the final SA",
)


