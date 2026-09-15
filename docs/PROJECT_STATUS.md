# Project Status

**Current stage:** Phase 1 — verified target inventory, binary mapping, and first source reconstruction

Nine directly supplied Pokémon Sapphire GBA images have been inventoried without committing ROM bytes. The project has moved from setup into active decompilation: reset/IRQ startup code, a revision-sensitive date routine, binary baselines, and revision deltas are now mapped from observed targets.

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

Exact CRC32, MD5, SHA-1, SHA-256, GBA header fields, and source filenames are recorded in `manifests/version-inventory.json`.

## Phase 1 findings

- All nine observed targets have valid GBA header complement checks.
- AXPJ revision 0 is an 8 MiB image; the other eight observed targets are 16 MiB.
- The observed reset path has two layouts. AXPJ/AXPE enter the ARM reset routine at ROM offset `0xD0`; AXPD/AXPF/AXPI enter at `0x204`.
- The common reset path establishes IRQ/System stacks, installs the BIOS IRQ callback, and enters the main Thumb code. Its first reconstruction is in `src/boot/boot_arm.S`.
- AXPI rev0→rev1 and AXPF rev0→rev1 each change exactly four bytes: revision/checksum bytes plus two Thumb conditional-branch condition bytes.
- AXPE rev1→rev2 has the same four-byte change pattern at the corresponding AXPE code location.
- Those two instruction changes preserve branch destinations while changing `BLE`→`BLT` and `BGT`→`BGE`.
- Surrounding code and data identify the affected function as a date/day-ordinal calculation: it uses a 365-day constant, a 12-entry month-length table, and a helper implementing divisibility-by-4/100/400 leap-year logic.
- The revision change corrects the prior-year loop boundary from `i > 0` to `i >= 0`. The first C reconstruction is in `src/reconstructed/date.c`.
- AXPE rev0 differs much more broadly from AXPE rev1/rev2 and must be treated as a distinct release layout rather than as only the four-byte date fix.

## Progress

- [x] Establish repository baseline and ROM/key exclusion rules
- [x] Inventory all nine currently supplied target builds
- [x] Record authoritative game code, revision, size, and cryptographic hashes
- [x] Generate first-pass 64 KiB block, ROM-pointer, and executable-signature baselines
- [x] Map same-game-code minor revision byte deltas
- [x] Reconstruct the common ARM reset/IRQ path at source level
- [x] Reconstruct the revision-sensitive leap-year/date-ordinal routine at C source level
- [ ] Reconstruct the Thumb entry path and early runtime initialization
- [ ] Classify ROM ranges into executable code, structured data, scripts, text, graphics, audio, and unused space
- [ ] Build function maps and cross-references for each release family
- [ ] Reconstruct game-data formats, maps, scripts/events, text, graphics, audio, save data, link/peripheral code, and unused/debug material
- [ ] Introduce target-aware build/link configuration
- [ ] Reach reproducible binary matching for reconstructed regions, then expand toward whole-ROM matching

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a supplied target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target bytes.

The current source reconstructions are **Observed/Reconstructed**, not yet byte-for-byte **Matched** builds. Semantic symbol names remain provisional until callers, data users, and matching compiler/linker behavior are established.

## Immediate next milestone

Continue from each target's Thumb entry point, recover the early runtime call graph, classify the first executable block, and connect the reconstructed date routine to its callers. In parallel, refine pointer clusters into named tables so code and data can be split into target-aware source files without committing retail ROM images.
