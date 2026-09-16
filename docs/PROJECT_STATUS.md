# Project Status

**Current stage:** Phase 1 — binary and container mapping

Nine directly supplied Pokémon Sapphire GBA images have been inventoried without committing ROM bytes. Phase 0 target identity for the currently supplied set is complete enough to proceed with Phase 1 mapping. Source reconstruction remains a later Phase 3 activity under the existing roadmap.

## Verified target inventory

| Target ID | Game code | Region / language | Revision | Size | Verification |
| --- | --- | --- | ---: | ---: | --- |
| `sapphire-axpd-rev1-de` | AXPD | Germany / German | 1 | 16 MiB | Observed |
| `sapphire-axpi-rev1-it` | AXPI | Italy / Italian | 1 | 16 MiB | Observed |
| `sapphire-axpj-rev0-ja` | AXPJ | Japan / Japanese | 0 | 8 MiB | Observed |
| `sapphire-axpe-rev1-en-eu` | AXPE | Europe / English | 1 | 16 MiB | Observed |
| `sapphire-axpf-rev0-fr` | AXPF | France / French | 0 | 16 MiB | Observed |
| `sapphire-axpi-rev0-it` | AXPI | Italy / Italian | 0 | 16 MiB | Observed |
| `sapphire-axpe-rev2-en-us-eu` | AXPE | USA/Europe / English | 2 | 16 MiB | Observed |
| `sapphire-axpe-rev0-en-us` | AXPE | USA / English | 0 | 16 MiB | Observed |
| `sapphire-axpf-rev1-fr` | AXPF | France / French | 1 | 16 MiB | Observed |

Exact source filenames, header fields, and cryptographic hashes are recorded in `manifests/version-inventory.json`.

## Phase 1 records

- `manifests/binary-baseline.json` — initial reset entry, 64 KiB block, aligned ROM-pointer, and Thumb-signature measurements for all nine targets.
- `manifests/revision-differences.json` — same-game-code byte and block comparisons, including decoded Thumb conditional-branch differences.
- `manifests/executable-map.json` — observed reset/IRQ/Thumb-entry and selected runtime offsets. Semantic symbol names are provisional pending Phase 2 context recovery.
- `tools/compare_revisions.py` — reproducible local revision comparison tool.

## Observed findings

- All nine observed targets have valid GBA header complement checks.
- AXPJ revision 0 is 8 MiB; the other eight observed targets are 16 MiB.
- The reset path currently separates into AXPJ/AXPE and AXPD/AXPF/AXPI layouts.
- AXPI rev0→rev1 and AXPF rev0→rev1 each differ by exactly four bytes: revision/checksum plus two Thumb conditional-branch condition bytes.
- AXPE rev1→rev2 shows the corresponding four-byte minor-revision pattern at AXPE-specific offsets.
- The two instruction changes preserve branch destinations while changing `BLE`→`BLT` and `BGT`→`BGE`.
- Surrounding code contains BCD conversion, calendar/leap-year operations, and a month-length table. These semantic labels are retained as provisional mapping evidence rather than promoted to reconstructed source during Phase 1.
- AXPE rev0 differs much more broadly from AXPE rev1/rev2 and must be treated as a distinct release layout during mapping.

## Progress

- [x] Establish repository baseline and ROM/key exclusion rules
- [x] Inventory all nine currently supplied target builds
- [x] Record game code, revision, size, header identity, and cryptographic hashes
- [x] Generate first-pass 64 KiB block, ROM-pointer, and executable-signature baselines
- [x] Record same-game-code minor revision byte deltas
- [x] Record initial reset/IRQ/Thumb entry offsets and selected executable relationships
- [ ] Classify ROM ranges into executable code, structured data, scripts, text, graphics, audio, and unused space
- [ ] Identify pointer tables, major structured tables, compression, packing, and serialization formats
- [ ] Complete Phase 1 binary/container mapping to a stable boundary
- [ ] Phase 2 — name functions, symbols, tables, and subsystems with evidence
- [ ] Phase 3 — reconstruct code, scripts, data tables, and asset metadata into source form
- [ ] Phase 4 — add repeatable matching and behavioral verification
- [ ] Phase 5 — provide documented build/repack workflow and CI where practical

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a supplied target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target bytes.

## Immediate next milestone

Continue Phase 1 only: refine the current block-level map into verified code/data/resource/unused ranges, identify pointer-table boundaries and major data containers, and record version-specific layout differences in the existing manifests and documentation. Do not establish a source-tree layout until the mapping and symbol context justify it.
