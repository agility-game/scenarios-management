# Way of Working

<img width="1488" height="653" alt="Image" src="https://github.com/user-attachments/assets/31d34b12-5dbc-47ef-820d-8e8f2c01ec4b" /><br/>
Source: [What's In My Toolkit - August 2025](https://hyperdev.matsuoka.com/p/whats-in-my-toolkit-august-2025)

## Goals

- Feature branches tied to specific issues with clear naming conventions.
- Commits that follow Conventional Commits format.
- GitHub issues structured with proper taxonomies and clear acceptance criteria.
- PRs that tell a coherent story of what changed and why.
- Zero drift between code changes and their documentation.

> Augment writes better tickets and manages Git better than I ever did.

- [Stop Using Git, Stop Writing Tickets.](https://hyperdev.substack.com/p/stop-using-git-stop-writing-tickets)

> AI agents are great at maintaining narrative discipline. They don't get tired, they don't skip steps, and they don't need calendar invites to stay aligned.

- [Training Your AI to Master Git & GitHub: The How-To Guide](https://hyperdev.matsuoka.com/p/how-i-trained-augment-code-to-run)

## Augment Workflow Guide

See [Augment Workflow Guide](https://github.com/vanHeemstraSystems/template-default-repository/.augment/workflow_guide.md), provide this guide to Augment.

When implementing this yourself, note that:

- You'll need a GitHub personal access token with appropriate permissions.
- Your AI assistant needs to understand API integration concepts.
- It helps to provide specific API endpoint references for GitHub.
- **Context window limits**: Your reference guide needs to fit within your AI's context window alongside actual work.
- **Technical prerequisites**: Your AI needs access to Git CLI commands and (optionally) GitHub's API.
- **Training approach**: Provide comprehensive documentation, not just isolated prompts.
- **Tool selection**: I've tested this with both Augment and Claude Code with similar results.
- **Iteration period**: Expect 1-2 weeks of refinement as you clarify instructions.

### Example Usage:

When you tell Augment "Create a decision log about our choice to use Firebase Auth," it drafts a comprehensive decision record that captures your rationale, alternatives considered, and implementation implications—all tagged properly as a decision issue.

## Takeaway

You don't need AI to write your code. (Though it should help with the first 70%)

You need it to maintain the narrative around your code—with consistency, structure, and purpose. You don't have to build a custom toolchain. You just need to treat your agent like a real team member:

- Provide comprehensive process documentation, see [Augment Workflow Guide](https://github.com/vanHeemstraSystems/template-default-repository/.augment/workflow_guide.md).
- Explain the "why" behind conventions.
- Let it own the narrative maintenance.
- Step in when high-impact decisions are needed.

## References

This article is part of our "[From the Trenches](https://hyperdev.substack.com/s/from-the-trenches)" series, featuring practical implementations of AI-powered development workflows. For more hands-on guides, check our archives.
