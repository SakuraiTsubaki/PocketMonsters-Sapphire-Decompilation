# Pocket Monsters Sapphire — Decompilation

![Status](https://img.shields.io/badge/status-Phase_1_active-blue)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![Verified targets](https://img.shields.io/badge/verified_targets-9-success)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon Sapphire**.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Keep analysis, tooling, metadata, and documentation reproducible.
- Progress from observed ROM structure to target-aware source builds and eventual binary matching.

## 🚧 Status

The project is in **Phase 1: verified binary mapping and source reconstruction**. Nine directly supplied Sapphire targets are inventoried by game code, revision, size, and cryptographic hashes. The common ARM reset/IRQ path and a revision-sensitive date/day-ordinal routine now have first source reconstructions.

Current reconstructed source:

- `src/boot/boot_arm.S` — common ARM reset and IRQ-dispatch path.
- `src/reconstructed/date.c` — leap-year helper and date/day-ordinal calculation, including the observed revision-dependent loop fix.

Current machine-readable analysis:

- `manifests/version-inventory.json` — exact identity of the nine observed targets.
- `analysis/phase-1/baseline-summary.json` — first-pass executable/pointer/block baseline.
- `analysis/phase-1/revision-deltas.json` — same-game-code revision differences.
- `analysis/phase-1/executable-map.json` — target-specific offsets and first semantic mappings.

## 🔎 First verified revision finding

AXPI rev0→rev1, AXPF rev0→rev1, and AXPE rev1→rev2 each contain a four-byte minor-revision delta: two header bytes plus two Thumb conditional-branch condition bytes. The code change preserves branch targets while changing `BLE`→`BLT` and `BGT`→`BGE` in the same date/day-ordinal routine, correcting its prior-year loop boundary from `i > 0` to `i >= 0`.

## 📌 Repository policy

ROM images and redistributed ROM binaries are **not included**. The repository stores reconstructed source, derived metadata, analysis, tooling, tests, documentation, and other reproducible project material. Original supplied ROMs remain local and read-only.

## 🧭 Roadmap

- [x] Establish baseline version/revision inventory
- [x] Map initial executable and revision-delta structures
- [x] Begin ARM/Thumb-to-source reconstruction
- [ ] Recover the early Thumb runtime call graph and classify executable/data ranges
- [ ] Reconstruct game data, scripts/events, maps, text, graphics, audio, save/link systems, and unused/debug material
- [ ] Add target-aware build/link configuration
- [ ] Add region-level and ultimately whole-target binary matching verification

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

Active areas include `src/`, `analysis/`, `tools/`, `manifests/`, and `docs/`. As formats are verified, the project will expand into `include/`, `data/`, `assets/`, and `tests/` without creating empty directory trees merely for appearance.

See [Repository Structure](docs/REPOSITORY_STRUCTURE.md) for the organization policy.

## 🔬 Research and verification

Findings identify the relevant target version or revision and separate hypotheses from observed, reproduced, or matched results. Current source reconstructions are not yet claimed as byte-for-byte matched builds; semantic names remain provisional where caller/context recovery is incomplete.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules, evidence expectations, commit guidance, and pull-request requirements.
