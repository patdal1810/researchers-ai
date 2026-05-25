import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    AGENTMIND_BASE_URL = os.getenv(
        "AGENTMIND_BASE_URL",
        "http://127.0.0.1:8000",
    )

    AGENTMIND_API_KEY = os.getenv(
        "AGENTMIND_API_KEY",
        "",
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        "",
    )

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-4.1-mini",
    )


settings = Settings()