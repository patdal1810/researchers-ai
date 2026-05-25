# ResearchOps AI Workflow Explanation

## Step 1 — Coordinator Receives Task

The coordinator agent receives the research objective and source list.

---

## Step 2 — RSS Scout Agent

The RSS Scout Agent scans RSS feeds and discovers candidate stories.

Tool used:
- rss_reader

---

## Step 3 — Story Ranking Agent

The Story Ranking Agent prioritizes stories based on:
- public impact
- keywords
- importance signals

Tool used:
- story_ranker

---

## Step 4 — Article Reader Agent

The Article Reader Agent reads full webpage content from selected URLs.

Tool used:
- url_reader

---

## Step 5 — Source Comparison Agent

The Source Comparison Agent groups duplicate or related stories.

Tool used:
- source_comparer

---

## Step 6 — Brief Writer Agent

The Brief Writer Agent creates the final intelligence brief.

---

## Step 7 — Content Strategy Agent

The Content Strategy Agent suggests:
- TikTok ideas
- YouTube angles
- social content hooks
