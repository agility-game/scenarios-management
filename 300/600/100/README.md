# 100 - Five Minute Tour

## Make sure you have Backlog.md installed

```
npm i -g backlog.md
```

## 1. Bootstrap a repo + backlog 

**Note**: Replace ```repository-name``` with the name of the current repository.

```
backlog init repository-name
```

## 2. Capture work

```
backlog task create "Title of an example task"
```

## 3. See where you stand

```
backlog board view
```

All data is saved under **backlog** folder in the root of the current repository as human‑readable Markdown with the following format ```task-<task-id> - <task-title>.md``` (e.g. task-12 - Fix typo.md).
