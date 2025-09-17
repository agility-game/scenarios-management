# Augment Workflow Guide

Based on [Training Your AI to Master Git & GitHub: The How-To Guide](https://hyperdev.matsuoka.com/p/how-i-trained-augment-code-to-run)

## 🔁 Git Workflow & Version Control

*We treat Git as a tool for narrating engineering decisions—not just storing code. Use it intentionally to reflect clarity, atomicity, and collaboration.*

### ✅ Commit Philosophy

- Commit early, commit often, but only once the change is coherent.
- Each commit should answer: What changed, and why?
- Prefer small, purposeful commits over monolithic ones.

### 🔤 Conventional Commit Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(optional-scope): short summary
[optional body]
[optional footer(s)]
```

**Examples**:

- feat(auth): add OAuth login
- fix(api): correct rate limit handling
- chore(lint): update prettier config

**Valid types**: feat, fix, chore, docs, refactor, test, perf, ci

### 🌱 Branch Naming Convention

Branches should reflect purpose and follow a type/slug format:

```
feature/search-api
fix/token-refresh
chore/update-deps
```

## 🧭 GitHub Issue Tracking

*We use **GitHub Issues** for all tracked work—features, bugs, ideas, spikes. Each issue answers: What are we doing, why does it matter, and how will we know it's done?*

### Issue Fields to Fill

- **Title** – human-readable and emoji-tagged (e.g. 🚀 Add login flow)
- **Description** – context, proposed approach, and acceptance criteria
- **Labels** – use taxonomy below
- **Assignee** – assign only when actively in progress
- **Milestone** – for cycles/themes

### Label Taxonomy

| Category | Prefix | Examples |
| --- | --- | --- |
| Theme | theme: | theme:infra, theme:ai, theme:ux |
| Status | status: | status:in-progress, status:blocked |
| Priority | prio: | prio:high, prio:low |
| Effort | size: | size:xs, size:m, size:xl |
| Type | type: | type:bug, type:feature, type:chore |

*Use emojis in titles for quick scan: 🧠, 🐛, 🚀, 📌, etc.*

## 📌 Decision Logs

Capture important architectural decisions as ```type:decision issues```.

- Title format: 📌 ```Decision: Move to Mastra```
- Rationale and trade-offs should be added in comments
