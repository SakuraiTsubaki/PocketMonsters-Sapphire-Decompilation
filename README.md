# Pocket Monsters Sapphire — Decompilation

![Status](https://img.shields.io/badge/status-Phase_1_binary_mapping-blue)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![Verified targets](https://img.shields.io/badge/verified_targets-9-success)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon Sapphire**.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Keep analysis, tooling, metadata, and documentation reproducible.
- Build a clean foundation for long-term reverse-engineering work.

## 🚧 Status

The project is in **Phase 1 — binary and container mapping**. Nine directly supplied Sapphire targets have been inventoried by game code, revision, size, and cryptographic hashes. Initial GBA entry-point, ROM-pointer, block, executable-offset, and same-game-code revision-difference mapping is recorded as machine-readable manifests.

No Phase 3 source-reconstruction layout is being established yet. Source directories will be introduced only when the Phase 1/2 mapping is sufficiently verified to justify the target-specific structure.

Current machine-readable project records:

- `manifests/version-inventory.json` — exact identity of the nine observed targets.
- `manifests/binary-baseline.json` — first-pass entry-point, pointer, block, and executable-signature baseline.
- `manifests/revision-differences.json` — same-game-code revision byte differences and decoded branch-condition changes.
- `manifests/executable-map.json` — observed target-specific runtime offsets and provisional semantic mappings.

Current Phase 1 tooling:

- `tools/inventory_target.py` — metadata-only target inventory.
- `tools/gba_baseline.py` — reproducible first-pass GBA binary map.
- `tools/compare_revisions.py` — same-size revision comparison and Thumb conditional-branch difference reporting.

## 🔎 Current verified findings

- All nine observed targets have valid GBA header complement checks.
- AXPJ revision 0 is 8 MiB; the other eight observed targets are 16 MiB.
- The reset-vector mapping separates AXPJ/AXPE from AXPD/AXPF/AXPI layouts.
- AXPI rev0→rev1, AXPF rev0→rev1, and AXPE rev1→rev2 each contain a four-byte minor-revision delta: two header bytes plus two Thumb conditional-branch condition-byte changes.
- The affected branch destinations are unchanged. The surrounding observed code is recorded in `manifests/executable-map.json`; semantic names remain provisional pending Phase 2 symbol/subsystem mapping.

## 📌 Repository policy

ROM images and redistributed ROM binaries are **not included**. The repository is intended for reconstructed source, extracted/recreated project data, tooling, analysis, documentation, manifests, and verification material. Original supplied ROMs remain local and read-only.

## 🧭 Roadmap

- [x] Establish and populate the supplied-target version/revision inventory
- [x] Begin Phase 1 binary mapping with repeatable tooling
- [x] Record initial executable offsets and revision-difference evidence
- [ ] Complete executable/data/resource/unused range classification
- [ ] Document containers, compression, packing, serialization, and major tables
- [ ] Phase 2: map symbols, functions, tables, subsystems, and dependencies
- [ ] Phase 3: begin target-aware source reconstruction
- [ ] Phase 4: add repeatable reconstruction verification
- [ ] Phase 5: provide reproducible build/repack workflow and CI where appropriate

## 📚 Documentation

| Document | Purpose |
| --- | --- |
| [Project status](docs/PROJECT_STATUS.md) | Current stage, coverage, validation level, and next milestones |
| [Roadmap](docs/ROADMAP.md) | Recommended decompilation phases and long-term progression |
| [Version coverage](docs/VERSIONS.md) | Regions, languages, revisions, updates, builds, and hashes |
| [Research guide](docs/RESEARCH_GUIDE.md) | Evidence, confidence, and research-recording workflow |
| [Verification guide](docs/VERIFICATION.md) | Standards for Observed, Reproduced, and Matched results |
| [Repository structure](docs/REPOSITORY_STRUCTURE.md) | Intended long-term source, data, asset, tooling, and manifest layout |
| [Documentation hub](docs/README.md) | Entry point for format, executable, script, asset, version, and verification notes |

## 🧱 Repository structure

The active Phase 1 areas are `tools/`, `manifests/`, and `docs/`. Future `src/`, `include/`, `data/`, `assets/`, and `tests/` directories are added only when they contain real verified project material and when their organization follows the mapped GBA target architecture.

See [Repository Structure](docs/REPOSITORY_STRUCTURE.md) for the organization policy.

## 🔬 Research and verification

Findings identify the relevant target version or revision and separate hypotheses from Observed, Reproduced, or Matched results. Offsets and semantic names that have not yet completed Phase 2 context recovery remain explicitly provisional.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules, evidence expectations, commit guidance, and pull-request requirements.
