# Master Visual Learning Skill V1.0

Portable, dependency-free **instruction package** for visual study notes, technical diagrams and presentations. Contains `SKILL.md`, nine module guides, config, decisions, QA, security, usage and local structural tests.

## Run local checks
`python -m unittest discover -s tests -v`

## Scope and limitations
No external repositories or binaries are included. No PDF/PPTX/HTML renderer is embedded. The host assistant must have suitable tools, and must obtain user approval before creating outputs. Structural tests do not establish visual quality, upstream security or full exporter functionality.

See `docs/repository-audit.md` and `docs/acceptance.md`.
