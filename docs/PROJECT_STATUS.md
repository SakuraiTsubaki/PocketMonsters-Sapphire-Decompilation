# Project Status

**Current stage:** Phase 0 — target identity / reproducibility baseline

The repository has moved beyond initial setup. Deterministic metadata-only target inventory tooling and CI are active. No retail target is treated as authoritative until its identity is recorded from directly observed local evidence.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Not yet inventoried | — | — | — | Unverified | Register only after direct inspection |

Machine-readable inventory: `manifests/version-inventory.json`

## Progress

- [x] Establish repository baseline and ROM/key exclusion rules
- [x] Add deterministic metadata-only target inventory tooling
- [x] Add CI for target inventory tooling
- [ ] Inventory the first verified target build
- [ ] Record authoritative region/language/revision/hash metadata
- [ ] Document ROM address-space and executable/data layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Add reproducible extraction/repacking tooling as formats are verified
- [ ] Add reconstruction matching verification

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.

## Immediate next milestone

Run `tools/inventory_target.py` against the first locally supplied Sapphire target, review the metadata-only output, register its exact identity, then begin the ROM/address-space map. Retail game bytes remain local and read-only.
