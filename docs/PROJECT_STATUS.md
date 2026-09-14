# Project Status

**Current stage:** Phase 0 — Target definition (in progress)

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

## Research baseline

This project currently assumes **no locally owned retail ROM image**. Research and reconstruction therefore begin from publicly available documentation, public reverse-engineering repositories, version/hash databases, hardware evidence, and reproducible derived work.

The original Japanese release is the historical comparison baseline. All confirmed regional, language, and revision branches are tracked separately rather than being silently merged into one generic Sapphire target.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon Sapphire | Japan | Japanese | Rev 0 / v1.0 | Observed | Primary historical baseline; `AGB-AXPJ-0`; SHA-1 recorded in `VERSIONS.md` |
| Pokémon Sapphire | Japan | Japanese | Rev 1 / v1.1 | Observed | Japanese revision branch; `AGB-AXPJ-1`; SHA-1 recorded in `VERSIONS.md` |
| Pokémon Sapphire | North America | English | Rev 0 | Reproduced upstream / local verification pending | `pret/pokeruby` matching target; public upstream SHA-1 known |
| Pokémon Sapphire | Other official regional/language branches | English/French/German/Italian/Spanish | Multiple | Observed / inventory in progress | Product-code/revision matrix seeded in `VERSIONS.md`; unresolved mappings remain explicit |

## Progress

- [x] Establish Japanese historical baseline identity for Sapphire Rev 0 and Rev 1
- [x] Seed first-pass official regional/revision branch inventory
- [x] Record initial public-source and hash provenance for the Japanese baseline
- [ ] Complete authoritative version/revision inventory for every official Sapphire branch
- [ ] Cross-verify every regional hash/product-code/revision mapping
- [ ] Reproduce and document Japanese Rev 0 ↔ Rev 1 differences
- [ ] Document executable and section layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Add reproducible extraction/repacking tooling
- [ ] Add automated verification where practical

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build, extracted data, authoritative documentation, or stable public identity evidence.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.

## Current evidence documents

- [`VERSIONS.md`](VERSIONS.md) — authoritative target/version inventory
- [`versions/JAPANESE_BASELINE.md`](versions/JAPANESE_BASELINE.md) — Japanese Sapphire baseline identity, provenance, public-source coverage, and open questions
- [`RESEARCH_GUIDE.md`](RESEARCH_GUIDE.md) — evidence and confidence rules
- [`VERIFICATION.md`](VERIFICATION.md) — verification requirements

## Next milestones

1. Finish Sapphire's complete region/language/revision identity matrix, including unresolved English `AXPE`/`AXPP` market-to-binary mappings.
2. Cross-check hashes and product identifiers from multiple independent public sources.
3. Document the Japanese Rev 0 ↔ Rev 1 delta and Berry/RTC fix at source/function level.
4. Inventory public Japanese Sapphire source/symbol/data research by subsystem.
5. Begin executable/data mapping only after target identities are stable enough to prevent cross-version contamination.

Update this file whenever the project reaches a meaningful milestone or adds a new supported target.
