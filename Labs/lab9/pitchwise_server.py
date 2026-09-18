
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("pitchwise-playbook")

# The Pitchwise partners' rubrics, one per pitch type.
# Each rubric has exactly three criteria the partners care about.
RUBRICS = {
    "consumer": {
        "name": "Consumer Product Pitch Rubric",
        "criteria": [
            "Hook: opens with a specific customer moment, not a category description.",
            "Why now: explains what changed in the world that makes this product possible or necessary right now.",
            "Distribution: names a concrete channel and explains why this product will travel through it.",
        ],
    },
    "b2b_saas": {
        "name": "B2B SaaS Pitch Rubric",
        "criteria": [
            "Customer pain: describes a real, named workflow the buyer hates today, not a vague 'inefficiency'.",
            "Market sizing: gives a concrete number of potential buyers and explains how it was estimated.",
            "Traction: cites a specific signal (a pilot, a paying customer, a signed letter of intent) instead of generic 'strong interest'.",
        ],
    },
    "deep_tech": {
        "name": "Deep Tech Pitch Rubric",
        "criteria": [
            "Technical edge: explains what the team can do that no one else can, in language a non-specialist can follow.",
            "Defensibility: names what protects the company from being copied (patents, proprietary data, specialized talent, hard-to-replicate process) and for how long.",
            "First customer: identifies a specific first buyer who would pay for an early version, not a 'future market'.",
        ],
    },
}

@mcp.tool()
def get_rubric(pitch_type: str) -> dict:
    """
    Return the Pitchwise scoring rubric for a given pitch type.

    Args:
        pitch_type: One of 'consumer', 'b2b_saas', or 'deep_tech'.

    Returns:
        dict: A dictionary with 'name' and 'criteria' keys, or
              {'name': 'Unknown', 'criteria': []} if pitch_type is not recognized.
    """
    return RUBRICS.get(pitch_type, {"name": "Unknown", "criteria": []})

if __name__ == "__main__":
    mcp.run()
