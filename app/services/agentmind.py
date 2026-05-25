from agentmind import AgentMindClient

from app.config.settings import settings


def get_agentmind_client() -> AgentMindClient:
    return AgentMindClient(
        base_url=settings.AGENTMIND_BASE_URL,
        api_key=settings.AGENTMIND_API_KEY or None,
        timeout=180,
    )


def get_llm_config() -> dict:
    return {
        "provider": "openai",
        "api_key": settings.OPENAI_API_KEY,
        "model": settings.OPENAI_MODEL,
    }