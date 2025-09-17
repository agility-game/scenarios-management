# Tooling

- [What's In My Toolkit - August 2025](https://hyperdev.matsuoka.com/p/whats-in-my-toolkit-august-2025)

## Integrated Development Environment (IDE)

### Claude Code & Claude MPM

Despite [Anthropic](https://anthropic.com/)'s recent hiccups with rate limiting and service stability, these remain the backbone of my development workflow. [Claude Code](https://claude.ai/code) handles the heavy lifting—complex refactoring, architectural discussions, multi-file changes that require deep context understanding.

[Claude MPM](https://github.com/bobmatnyc/claude-mpm) (Robert (Masa) Matsuoka - aka bobmatnyc - own orchestration framework) comes into play for larger projects where coordination between multiple agents provides better results than single-threaded development. Gives me both direct control and systematic automation.

Why I stick with them: When they work, they work better than anything else. Context window, reasoning quality, and code understanding remain unmatched. But I've learned to have backups ready.

### Augment Code

- [Augment (a better Cursor)](https://augmentcode.com): AI-enabled Integrated Development Environment

My $50/month insurance policy turned daily tool. Augment Code is fast, reliable, particularly effective for focused troubleshooting sessions where I need quick, targeted solutions rather than comprehensive analysis.

The remote agents feature has become unexpectedly useful — I can queue up documentation tasks or code cleanup while my laptop is closed or I'm in meetings. Not some massive productivity boost, but consistently useful.

When I reach for it: Quick debugging sessions, remote work when I can't keep the laptop running, sanity check when Claude Code responses feel off.

### Claude.AI (Web + Desktop)

My day starts and ends here. Morning routine involves research, planning, workflow integration with Linear. Evening winds down with notes consolidation, often pulling in recordings from Granola to create actionable summaries.

The [Claude.AI](https://claude.ai/) desktop app stays available for those "quick question" moments that inevitably turn into deeper strategy discussions. I find myself using it for meta-thinking about projects—not just execution, but planning the execution.

Daily pattern: Research and planning in the morning, integration work throughout the day, synthesis and notes in the evening.

<img width="1488" height="653" alt="Image" src="https://github.com/user-attachments/assets/31d34b12-5dbc-47ef-820d-8e8f2c01ec4b" />

### Warp Terminal

Works well for CLI work. [Warp](https://warp.dev/) provides AI command suggestions, modern interface, and workflow features that make terminal operations more efficient. AI integration helps with complex git operations and system administration tasks.

Why not iTerm2 or default Terminal: The AI assistance for command construction and the modern UX eliminate friction from terminal work. Small improvements that compound over dozens of daily interactions.

## Meetings

### Granola: for most meetings and client calls

Different tools for different meeting types. [Granola](https://granola.ai/) wins for its flexibility — works with any meeting platform, captures everything, transcription quality is solid for most scenarios.

### Fireflies: when I need the data to flow into other systems

[Fireflies](https://fireflies.ai/) gets the nod when I need programmatic access to meeting data. Their GraphQL API makes it easy to pull transcripts into workflows, analyze recurring themes, build custom reporting. Less ubiquitous than Granola, but better for systematic processing.

## Voice Prompting: Voice, Don't Text

### SuperWhisper

This changed how I work more than I expected. Instead of typing out prompts, comments, or documentation notes, I dictate them. [SuperWhisper](https://superwhisper.com/) is particularly effective for meta-prompting—describing complex coding tasks in natural language before translating them into structured instructions.

Quality is good enough that I rarely edit the output. Significantly faster than typing for anything longer than a few sentences.

Primary uses: Writing documentation, creating detailed prompts for coding tasks, initial brain-dumps of technical requirements.

## Project Management

### Linear

As a long-time JIRA sufferer, [Linear](https://linear.app/) actually works. Clean interface, developer-focused design, none of the enterprise bloat that makes task management a chore.

The real win is the MCP connector. I can create issues, update statuses, query project state directly through Claude.AI. Planning sessions become conversations where I can immediately capture decisions as properly structured tasks without context switching.

JIRA escape: No more wrestling with complex workflows designed for enterprise bureaucracy. Linear keeps the focus on shipping code, not managing processes.

## Email

### Spike: Email Consolidation

I run about ten different email accounts across clients, projects, and business functions. [Spike](https://spikenow.com/) consolidates them into something manageable with a chat-like interface that makes email feel less overwhelming.

Not technically a development tool, but email management directly impacts productivity. When you're juggling multiple client relationships and project communications, unified inbox management becomes necessary infrastructure.

## Hardware

## MacBook Air M4 (32GB RAM)

Everything runs on a MacBook Air M4 with 32GB of RAM. Amazing what's possible with such a lightweight machine when you configure it properly.

The 32GB is non-negotiable if you're running multiple AI tools simultaneously. Claude Code, Augment Code, browser tabs, development environments, meeting tools all demand memory. 16GB works until it doesn't, and when it doesn't, you lose productivity immediately.

Performance reality: Local development environments, multiple AI tool sessions, browser-based research, background agents all run smoothly. The M4 handles compilation and testing without thermal throttling. For development work that doesn't require massive local compute, it's impressive.

## How This Fits Together

1) SuperWhisper dictates initial requirements into Claude.AI for planning. 
2) That planning flows to Claude Code for implementation.
3) Augment Code handles edge cases and quick fixes.
4) Meeting intelligence tools capture client feedback and discussions.
5) Everything runs smoothly on the M4 with enough RAM to avoid bottlenecks.

Not the most complex setup, but it handles the full development lifecycle from initial client conversations through production deployment.

Coming up: Detailed looks at specific workflow integrations, productivity measurements from different tool combinations, deep dives into the tools that prove most valuable over time. Watch [this space](https://substack.com/@bobmatnyc/posts).
