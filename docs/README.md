# Documentation Hub

This directory is the central documentation portal for the decompilation project. Use it to move from public-source census and target identification through reconstruction, asset handling, manifests, and verification without losing version context or evidence.

## Quick links

| Document | Purpose |
| --- | --- |
| [Public Source Inventory](SOURCE_INVENTORY.md) | Exhaustive public-source coverage ledger, source-family status, provenance, duplicates, conflicts, gaps, and search-log requirements |
| [Project Status](PROJECT_STATUS.md) | Current stage, target coverage, validation level, and next milestones |
| [Roadmap](ROADMAP.md) | Project phases beginning with exhaustive public-source census and target definition |
| [Version Coverage](VERSIONS.md) | Regions, languages, revisions, updates, builds, hashes, and support status |
| [Research Guide](RESEARCH_GUIDE.md) | Evidence, confidence, offsets, naming, and research-recording practices |
| [Verification Guide](VERIFICATION.md) | Standards for Unverified, Observed, Reproduced, and Matched results |
| [Repository Structure](REPOSITORY_STRUCTURE.md) | Intended long-term layout for source, data, assets, tools, tests, and manifests |
| [Project Standards](PROJECT_STANDARDS.md) | Naming, provenance, generated-data, manifest, and repository-boundary rules |
| [Asset Workflow](ASSET_WORKFLOW.md) | Extraction, reviewable assets, deduplication, manifest registration, and batch workflow |
| [Manifest Guide](../manifests/README.md) | Machine-readable inventories, hashes, target coverage, provenance, and shared assets |
| [Contributing](../CONTRIBUTING.md) | Contribution rules, evidence expectations, commits, and pull-request guidance |

## Research areas

As verified work becomes concrete, documentation may grow into areas such as `architecture/`, `formats/`, `research/`, `versions/`, `sources/`, and `verification/`. Create these directories when they contain real research material rather than as empty placeholders.

## Recommended documentation flow

1. Survey and register public evidence in `SOURCE_INVENTORY.md`; do not treat representative sources as exhaustive coverage.
2. Identify the exact target in `VERSIONS.md`, using the Japanese release as the historical baseline while preserving every regional/language/revision branch separately.
3. Record investigation methods and evidence according to `RESEARCH_GUIDE.md`.
4. Reconstruct source, data, or assets following `PROJECT_STANDARDS.md` and `REPOSITORY_STRUCTURE.md`.
5. For asset work, follow `ASSET_WORKFLOW.md` and register material in `../manifests/`.
6. Apply the validation levels defined in `VERIFICATION.md`.
7. Update `PROJECT_STATUS.md`, `ROADMAP.md`, `VERSIONS.md`, and `SOURCE_INVENTORY.md` whenever meaningful coverage changes.

## Documentation rules

- Distinguish confirmed findings from hypotheses.
- Identify the exact target version or revision for version-specific claims.
- Record offsets, paths, symbols, hashes, commands, URLs, publication identities, and other stable evidence when practical.
- Record search gaps and negative results instead of silently treating them as absence.
- Distinguish independent evidence from mirrors, forks, copies, hacks, and derivative projects.
- Use `TBD`, `unknown`, or `null` instead of inventing missing information.
- Preserve enough provenance for another researcher to reproduce or verify the finding.
- Keep retail ROM images, decrypted game images, console keys, and other redistributable game binaries out of the repository.