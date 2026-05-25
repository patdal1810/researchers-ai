from fastapi import FastAPI

app = FastAPI(
    title="Fake ResearchOps APIs",
    description="Mock ranking and source comparison APIs for ResearchOps AI.",
)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "Fake ResearchOps APIs running.",
    }


@app.post("/story-ranker")
def story_ranker(payload: dict):
    stories = payload.get("stories", [])

    ranked = []

    for index, story in enumerate(stories):
        title = str(story.get("title", "")).lower()
        score = 50

        if any(word in title for word in ["breaking", "crisis", "election", "ai", "fraud"]):
            score += 30

        if any(word in title for word in ["economy", "business", "security", "policy"]):
            score += 20

        ranked.append(
            {
                **story,
                "importance_score": min(score, 100),
                "rank_reason": "Ranked based on title keywords and public impact signals.",
            }
        )

    ranked.sort(
        key=lambda item: item.get("importance_score", 0),
        reverse=True,
    )

    return {
        "ranked_stories": ranked,
    }


@app.post("/source-comparer")
def source_comparer(payload: dict):
    stories = payload.get("stories", [])

    groups = {}

    for story in stories:
        title = story.get("title", "Untitled")
        first_word = title.split(" ")[0].lower() if title else "unknown"

        groups.setdefault(first_word, []).append(story)

    return {
        "groups": [
            {
                "group_key": key,
                "stories": value,
                "summary": f"{len(value)} related stories grouped under '{key}'.",
            }
            for key, value in groups.items()
        ]
    }