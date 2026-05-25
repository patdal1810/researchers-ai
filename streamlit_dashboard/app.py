import requests
import streamlit as st


RESEARCHOPS_API_URL = "http://127.0.0.1:8200"

st.set_page_config(
    page_title="ResearchOps AI",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 ResearchOps AI")
st.caption("Agentic research intelligence platform powered by AgentMind.")


TEST_CASES = {
    "AI + Tech News": {
        "topic": "AI and technology news",
        "sources": [
            "https://techcrunch.com/feed/",
            "https://feeds.feedburner.com/TechCabal",
            "https://www.theverge.com/rss/index.xml",
        ],
        "max_stories": 5,
    },
    "Nigeria Business News": {
        "topic": "Nigeria business and economy news",
        "sources": [
            "https://punchng.com/feed/",
            "https://www.vanguardngr.com/feed/",
        ],
        "max_stories": 5,
    },
}


def post_research(payload: dict):
    response = requests.post(
        f"{RESEARCHOPS_API_URL}/researchops/run",
        json=payload,
        timeout=240,
    )

    if not response.ok:
        st.error(f"ResearchOps API error: {response.status_code}")
        st.code(response.text)
        response.raise_for_status()

    return response.json()


def render_metrics(agentmind_result: dict):
    tool_calls = agentmind_result.get("tool_calls", [])

    delegations = [
        call for call in tool_calls
        if call.get("tool_name") == "delegate_task"
    ]

    nested_tools = []

    for call in delegations:
        result = call.get("result") or {}
        nested_tools.extend(result.get("tool_calls") or [])

    col1, col2, col3 = st.columns(3)

    col1.metric("Delegations", len(delegations))
    col2.metric("Specialist Tool Calls", len(nested_tools))
    col3.metric("Status", "Completed")


def render_timeline(agentmind_result: dict):
    st.subheader("Agent Research Timeline")

    tool_calls = agentmind_result.get("tool_calls", [])

    if not tool_calls:
        st.warning("No agent activity found.")
        return

    for index, call in enumerate(tool_calls, start=1):
        result = call.get("result") or {}

        with st.container(border=True):
            st.markdown(f"### Step {index}: {call.get('tool_name')}")
            st.write(f"**Status:** {call.get('status')}")

            if call.get("tool_name") == "delegate_task":
                st.write(f"**Target agent:** {result.get('target_agent_name')}")
                st.write(f"**Reason:** {result.get('delegation_reason')}")

                child_calls = result.get("tool_calls") or []

                if child_calls:
                    st.markdown("**Specialist tools used:**")

                    for child in child_calls:
                        st.write(
                            f"- `{child.get('tool_name')}` → "
                            f"**{child.get('status')}**"
                        )

                        with st.expander(f"View {child.get('tool_name')} details"):
                            st.json(child)

                with st.expander("View agent response"):
                    st.write(result.get("response"))

            else:
                st.json(call)


selected_case = st.selectbox(
    "Choose research test case",
    list(TEST_CASES.keys()),
)

payload = TEST_CASES[selected_case]

st.subheader("Research Topic")
st.write(payload["topic"])

st.subheader("Sources")
st.json(payload["sources"])

st.subheader("Max Stories")
st.code(payload["max_stories"])

if st.button("Run ResearchOps Workflow", type="primary"):
    with st.spinner("Research agents are monitoring, ranking, comparing, and writing..."):
        result = post_research(payload)

    st.success("Research workflow completed.")

    workflow_id = result.get("workflow_id")
    agentmind_result = result.get("result", {})

    st.subheader("Workflow ID")
    st.code(workflow_id)

    st.subheader("Final Intelligence Brief")
    st.write(agentmind_result.get("response"))

    st.divider()

    render_metrics(agentmind_result)

    st.divider()

    render_timeline(agentmind_result)

    with st.expander("Raw Result"):
        st.json(result)