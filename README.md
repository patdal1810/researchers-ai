# ResearchOps AI

Autonomous research intelligence platform powered by AgentMind.

## Features

- Multi-agent orchestration
- RSS monitoring
- Story ranking
- URL article reading
- Source comparison
- Intelligence brief generation
- Streamlit dashboard
- Workflow delegation
- Webhook tools

## Agent Flow

Coordinator Agent
→ RSS Scout Agent
→ Story Ranking Agent
→ Article Reader Agent
→ Source Comparison Agent
→ Brief Writer Agent
→ Content Strategy Agent

## Running the System

### AgentMind Backend

```bash
python -m uvicorn app.main:app --reload --port 8000
```

### Fake Research APIs

```bash
python -m uvicorn fake_research_apis.main:app --reload --port 9100
```

### ResearchOps Backend

```bash
python -m uvicorn app.main:app --reload --port 8200
```

### Streamlit Dashboard

```bash
streamlit run streamlit_dashboard/app.py
```

## Example Workflow

Research topic:
- AI and technology news

Sources:
- TechCrunch
- The Verge
- TechCabal

Workflow:
1. RSS feeds scanned
2. Stories ranked
3. Articles read
4. Sources compared
5. Intelligence brief generated
6. Content angles suggested
