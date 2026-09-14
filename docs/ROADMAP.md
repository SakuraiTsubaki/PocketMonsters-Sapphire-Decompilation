# Roadmap

This roadmap defines the recommended order for turning this repository from an initial research scaffold into a reproducible decompilation project.

## Phase 0 — Public-source census and target definition

- [ ] Exhaustively survey publicly accessible source families relevant to Pokémon Sapphire, beginning from the original Japanese release and tracing every confirmed regional, language, revision, distribution, peripheral, and linked-system variant.
- [ ] Maintain `SOURCE_INVENTORY.md` as the authoritative source-coverage ledger, including searched, reviewed, duplicate, derivative, conflicting, inaccessible, dead, and negative-result records.
- [ ] Identify authoritative game versions, regions, languages, revisions, and updates.
- [ ] Record hashes, product codes, dates, provenance, and physical/revision evidence for each supported target when publicly verifiable.
- [ ] Separate independent evidence from mirrors, forks, copies, hacks, and derivative projects.
- [ ] Define the Japanese release baseline and document how every later regional target differs from or relates to it.
- [ ] Do not mark Phase 0 complete merely because representative sources have been found; completion requires the documented source-family coverage matrix to be exhausted to the recorded search date.

## Phase 1 — Binary and container mapping

- [ ] Document executable layout, sections, archives, resource containers, and GBA-specific memory/data organization using verified public evidence.
- [ ] Build file/data manifests and extraction/reconstruction notes.
- [ ] Record known compression, packing, serialization, save, link, and peripheral formats.
- [ ] Keep region/language/revision-specific layouts separate whenever evidence shows differences.

## Phase 2 — Symbol and subsystem mapping

- [ ] Name functions, symbols, tables, and major data structures.
- [ ] Identify engine subsystems and dependencies.
- [ ] Track confidence and evidence for each finding.
- [ ] Compare Japanese-baseline structures against every documented regional branch.

## Phase 3 — Source reconstruction

- [ ] Reconstruct code into readable, maintainable source.
- [ ] Reconstruct scripts, data tables, text, maps, graphics, audio metadata, events, and asset metadata.
- [ ] Add extraction/repacking/conversion tools where needed.
- [ ] Preserve verified regional and revision differences instead of flattening them into one build.

## Phase 4 — Verification

- [ ] Add repeatable tests and comparison workflows.
- [ ] Track matching or behavioral-equivalence status by target and subsystem.
- [ ] Document remaining mismatches, conflicts, unknowns, and evidence gaps.
- [ ] Never promote an inferred Japanese/regional relationship to fact without evidence.

## Phase 5 — Reproducible project workflow

- [ ] Provide documented setup and build/repack steps where reconstruction permits them.
- [ ] Add CI or automated verification where practical.
- [ ] Keep generated outputs reproducible from repository sources and tooling.
- [ ] Keep retail ROM images and other redistributable game binaries out of the repository while retaining lawful metadata, hashes, provenance, reconstructed source, research, and project-created outputs.

Update this roadmap whenever public-source coverage, target coverage, or reconstruction status materially changes.