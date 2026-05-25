import os

from dotenv import load_dotenv

from agentmind import AgentMindClient

load_dotenv()

AGENTMIND_BASE_URL = os.getenv(
    "AGENTMIND_BASE_URL",
    "http://127.0.0.1:8000",
)

AGENTMIND_API_KEY = os.getenv(
    "AGENTMIND_API_KEY",
)

INVITE_CODE = os.getenv(
    "AGENTMIND_INVITE_CODE",
    "AGENTMIND-BETA-001",
)

client = AgentMindClient(
    base_url=AGENTMIND_BASE_URL,
    api_key=AGENTMIND_API_KEY,
)


def register_tools():
    story_ranker_schema = {
        "type": "object",
        "properties": {
            "stories": {
                "type": "array",
                "items": {
                    "type": "object",
                },
            },
        },
        "required": ["stories"],
    }

    source_comparer_schema = {
        "type": "object",
        "properties": {
            "stories": {
                "type": "array",
                "items": {
                    "type": "object",
                },
            },
        },
        "required": ["stories"],
    }

    client.register_tool(
        name="story_ranker",
        description=(
            "Ranks stories by estimated public importance and impact."
        ),
        permission_required="tools:story_ranker:run",
        input_schema=story_ranker_schema,
        is_webhook=True,
        webhook_url="http://127.0.0.1:9100/story-ranker",
    )

    client.register_tool(
        name="source_comparer",
        description=(
            "Groups and compares related stories from multiple sources."
        ),
        permission_required="tools:source_comparer:run",
        input_schema=source_comparer_schema,
        is_webhook=True,
        webhook_url="http://127.0.0.1:9100/source-comparer",
    )

    print("ResearchOps tools registered.")


def register_agents():
    coordinator = client.register_agent(
        name="ResearchOps Coordinator Agent",
        purpose=(
            "Coordinates research workflows and delegates work "
            "to specialist research agents."
        ),
        invite_code=INVITE_CODE,
        capabilities=[
            "coordination",
            "delegation",
            "research_operations",
            "workflow_management",
        ],
        permissions=[
            "agents:delegate",
            "memory:read",
            "memory:write",
        ],
    )

    client.register_agent(
        name="RSS Scout Agent",
        purpose=(
            "Scans RSS feeds and discovers important stories."
        ),
        invite_code=INVITE_CODE,
        capabilities=[
            "rss_monitoring",
            "news_discovery",
            "feed_analysis",
        ],
        permissions=[
            "tools:rss_reader:run",
            "memory:read",
            "memory:write",
        ],
    )

    client.register_agent(
        name="Article Reader Agent",
        purpose=(
            "Reads webpages and extracts important content."
        ),
        invite_code=INVITE_CODE,
        capabilities=[
            "article_reading",
            "webpage_analysis",
            "content_extraction",
        ],
        permissions=[
            "tools:url_reader:run",
            "memory:read",
            "memory:write",
        ],
    )

    client.register_agent(
        name="Story Ranking Agent",
        purpose=(
            "Ranks stories by public importance and impact."
        ),
        invite_code=INVITE_CODE,
        capabilities=[
            "story_ranking",
            "impact_analysis",
            "priority_scoring",
        ],
        permissions=[
            "tools:story_ranker:run",
            "memory:read",
            "memory:write",
        ],
    )

    client.register_agent(
        name="Source Comparison Agent",
        purpose=(
            "Groups related stories and compares source overlap."
        ),
        invite_code=INVITE_CODE,
        capabilities=[
            "source_comparison",
            "duplicate_detection",
            "story_grouping",
        ],
        permissions=[
            "tools:source_comparer:run",
            "memory:read",
            "memory:write",
        ],
    )

    client.register_agent(
        name="Brief Writer Agent",
        purpose=(
            "Creates final intelligence research briefs."
        ),
        invite_code=INVITE_CODE,
        capabilities=[
            "brief_writing",
            "executive_summary",
            "research_reporting",
        ],
        permissions=[],
    )

    client.register_agent(
        name="Content Strategy Agent",
        purpose=(
            "Suggests content ideas and social media angles "
            "based on research findings."
        ),
        invite_code=INVITE_CODE,
        capabilities=[
            "content_strategy",
            "viral_content",
            "media_planning",
        ],
        permissions=[],
    )

    print("ResearchOps agents registered.")

    print("\nCoordinator API Key:")
    print(coordinator["api_key"])

    return coordinator


if __name__ == "__main__":
    print("Setting up ResearchOps AI...")

    print("AgentMind base URL:", AGENTMIND_BASE_URL)
    print("AgentMind API key exists:", bool(AGENTMIND_API_KEY))
    
    print("\nCurrent setup agent:")
    print(client.me())

    print("\nCurrent tools:")
    print(client.list_tools())

    register_tools()

    coordinator = register_agents()

    print("\nSetup complete.")