# Further Reading

## Offiziell

- GitHub Spec Kit (Spec-Driven Development Toolkit): <https://github.com/github/spec-kit/blob/main/spec-driven.md>
- OpenSpec (Repo-lokale Specs & Change-Artefakte): <https://openspec.dev/>
- Codex Subagents & Workflows: <https://developers.openai.com/codex/subagents> & <https://developers.openai.com/codex/workflows>
- Claude Code Feature Overview (Plan Mode, Subagents, Agent Teams, Hooks): <https://code.claude.com/docs/en/features-overview>
- GitHub Copilot Custom Agents: <https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents>

## Vertiefung im Repo

- [Superpowers Hands-on](../../resources/superpowers-hands-on.md): Erzwingt Brainstorming -> Plan -> TDD -> Code Review als installierbares Skill-Bündel.
- [OpenSpec Hands-on](../../resources/openspec-hands-on.md): Verwaltet Proposal, Spec-Deltas, Design und Tasks als strukturierte Dateien im Repo.
- [Workflow Comparison Lab](../../resources/workflow-comparison-lab.md): Vergleicht manuelles SDD, Superpowers und OpenSpec am selben Change.

## Reflexionsfrage für dein Team

Welcher Übergang spart in eurer Codebase am meisten Nacharbeit:
1. **Explore -> Specify** (Spec-Datei vor Code)
2. **Plan -> Lock** (3-Schritte-Plan abnicken vor dem ersten Edit)
3. **Execute -> Independent Audit** (frischer Reviewer-Agent prüft `git diff` gegen die Spec)?
