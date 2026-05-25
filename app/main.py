from fastapi import FastAPI

from app.services.agentmind import (
    get_agentmind_client,
    get_llm_config,
)


app = FastAPI(
    title="ResearchOps AI",
    description="Agentic research intelligence platform powered by AgentMind.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "ResearchOps AI backend is running.",
    }


@app.get("/health/agentmind")
def check_agentmind():
    client = get_agentmind_client()
    return client.health_check()


@app.post("/researchops/run")
def run_researchops(payload: dict):
    client = get_agentmind_client()

    sources = payload.get("sources", [])
    topic = payload.get("topic", "general news")
    max_stories = payload.get("max_stories", 5)

    workflow = client.create_workflow(
        (
            "Monitor multiple information sources, rank important stories, "
            "compare related stories, and generate a research intelligence brief."
        )
    )

    workflow_id = workflow["result"]["workflow_id"]

    task = (
        "You are the ResearchOps Coordinator Agent.\n\n"
        "Use the best available specialist agents and tools based on their "
        "capabilities, permissions, and descriptions.\n\n"
        "Goal:\n"
        f"- Research topic: {topic}\n"
        f"- Sources: {sources}\n"
        f"- Maximum stories to analyze: {max_stories}\n\n"
        "Required workflow:\n"
        "1. Ask an RSS-capable agent to scan the provided sources.\n"
        "2. Ask a ranking-capable agent to rank important stories.\n"
        "3. Ask an article-reading agent to read selected article URLs when available.\n"
        "4. Ask a comparison-capable agent to group related/duplicate stories.\n"
        "5. Ask a brief-writing agent to create a daily intelligence brief.\n"
        "6. Ask a content strategy agent to suggest content angles.\n\n"
        "Final output must include:\n"
        "- Top stories\n"
        "- Why they matter\n"
        "- Related source grouping\n"
        "- Key risks or opportunities\n"
        "- 5 content ideas\n"
    )

    result = client.run_task(
        task=task,
        memory_search_limit=5,
        save_result_to_memory=True,
        workflow_id=workflow_id,
        llm_config=get_llm_config(),
    )

    return {
        "success": True,
        "workflow_id": workflow_id,
        "result": result,
    }


@app.get("/researchops/workflows/{workflow_id}")
def get_researchops_workflow(workflow_id: int):
    client = get_agentmind_client()

    workflow = client.get_workflow(workflow_id)

    return {
        "success": True,
        "workflow_id": workflow_id,
        "workflow": workflow,
    }