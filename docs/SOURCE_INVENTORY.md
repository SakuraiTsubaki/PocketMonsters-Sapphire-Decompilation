# Public Source Inventory

This document is the authoritative coverage ledger for public-source research used by the Pocket Monsters Sapphire decompilation project.

## Research premise

The project does **not** assume access to a retail ROM image. Research begins from publicly accessible evidence and reconstructed material. The historical Japanese release is the primary baseline, and every confirmed regional, language, revision, distribution, peripheral, and linked-system variant is traced from that baseline.

A small set of representative sources is **not** an exhaustive survey. This inventory remains incomplete until every source family below has been searched, reviewed, deduplicated, cross-checked, and either linked to findings or explicitly recorded as yielding no usable evidence.

## Completion rule

Do not describe Phase 0 source research as complete unless all of the following are true:

1. Every source family in the coverage matrix has been searched with Japanese and non-Japanese queries where relevant.
2. Candidate sources have been opened and reviewed, not merely returned by a search engine.
3. Mirrors, forks, copies, and derivative projects have been identified so duplicated evidence is not counted as independent confirmation.
4. Conflicting claims have been recorded and resolved where possible by version, region, language, revision, platform, or date.
5. Sources that cannot be verified are retained as `unverified` rather than silently discarded.
6. Material that is publicly discoverable but not suitable for redistribution is indexed by provenance and metadata rather than mirrored.
7. Search gaps and negative results are recorded explicitly.
8. Newly discovered sources remain eligible for addition; `complete` means complete against the documented search universe and date, not that no future source can ever appear.

## Coverage matrix

| Source family | Required coverage | Current status |
| --- | --- | --- |
| Official Pokémon Japan | Product pages, historical game pages, event notices, support notices, peripherals | In progress |
| Nintendo Japan | Product pages, support pages, Berry-related notices, peripheral/link documentation | In progress |
| Official international Pokémon/Nintendo sites | North America, Europe, Australia and language-specific historical pages | Not yet exhaustive |
| Archived official web | Wayback/other archival captures of removed or changed official pages | Not yet exhaustive |
| Manuals / packaging / inserts | Japanese baseline first, then every official regional/language edition | Not yet exhaustive |
| Official guides / magazines / promotional material | Release, event, e-Reader, distribution and revision evidence | Not yet exhaustive |
| Upstream decompilation/disassembly | pret and other independent projects; files, branches, history, issues and PRs | In progress |
| Forks and derivative source projects | Useful recovered symbols/data/tools; distinguish hacks from original evidence | Not yet exhaustive |
| Preservation databases | No-Intro/Dat-o-Matic, cartridge/board databases, hashes, product codes, revisions | In progress |
| Physical cartridge evidence | Label codes, revision stamps, PCB/ROM/flash/RTC photos and component data | In progress |
| Technical hardware documentation | GBA header, Flash/RTC, link cable, multiboot, Wireless Adapter, e-Reader | Not yet exhaustive |
| Save/data-format research | Save sections, checksums, Pokémon structures, event structures, record mixing | In progress |
| Mystery Event / Mystery Gift research | Scripts, flags, Wonder Card/News, distribution mechanics, regional differences | In progress |
| Official event/distribution preservation | Eon Ticket and all Gen III distributions linked to Sapphire; metadata and provenance | In progress |
| e-Reader / e-Card research | Japanese/English cards, dot-code formats, Battle-e, berries, decorations, trainers | In progress |
| Berry glitch / update programs | Original bug, revisions, Berry Program Update, multiboot implementations | In progress |
| GameCube linkage | Colosseum, XD, Box, Channel and Bonus Disc interactions relevant to Sapphire | Not yet exhaustive |
| Unused/debug/prototype research | TCRF, debug symbols/text, unused maps/data/music/graphics, demos/kiosk builds | Not yet exhaustive |
| Bug and revision research | Original behavior, region/revision fixes, side effects | Not yet exhaustive |
| Graphics/maps/audio/text datasets | Extracted or reconstructed assets, maps, scripts, sound/music metadata | Not yet exhaustive |
| Community reference databases | Bulbapedia, Serebii and language-specific wikis as leads/cross-checks | In progress |
| Forums/personal research archives | Project Pokémon, ROM-hacking communities, old technical sites, archived threads | In progress |
| Video/photo evidence | Hardware, kiosk, distribution and event operation where primary artifacts are unavailable | Not yet exhaustive |
| Academic/patent/standards material | Relevant technical documentation when it materially supports implementation | Not yet exhaustive |

## Sources registered so far

The entries below are **seed records**, not a claim of completeness.

| ID | Source | Class | Scope / value | Verification |
| --- | --- | --- | --- | --- |
| OFF-JP-PKM-RS | https://www.pokemon.co.jp/game/gba/rs/ | Official | Japanese Ruby/Sapphire product baseline, release/platform/peripheral metadata | Observed |
| SRC-PRET-RS | https://github.com/pret/pokeruby | Source reconstruction | Major public Ruby/Sapphire decompilation baseline; target/language/revision support must be checked file-by-file | Observed |
| SRC-PRET-BERRY | https://github.com/pret/berry-fix | Source reconstruction | Berry Fix multiboot program research relevant to Ruby/Sapphire RTC/berry update behavior | Observed |
| PRES-GEKKIO-AXPJ | https://gbhwdb.gekkio.fi/cartridges/AGB-AXPJ-0/ | Preservation / physical | Japanese Sapphire cartridge identity, board/components and revision evidence | Observed |
| RE-PP-MYSTERY | https://projectpokemon.org/home/forums/topic/35903-gen-3-mystery-eventgift-research/ | Reverse engineering | Gen III Mystery Event/Gift structures, scripts, flags, distributions and regional behavior | Observed |
| EVT-PP-COMP | https://projectpokemon.org/home/files/file/3277-pokemon-generation-iii-event-compilation-savefiles/ | Preservation / event | Event-Pokémon provenance leads across GBA/GameCube sources; per-entry authenticity requires checking | Observed |

## Evidence handling

- Official sources establish release, product, peripheral and event claims when available.
- Reproducible source projects can establish code/data structure only for the exact target they match; support for one language or revision must never be generalized to all releases.
- Community wikis are discovery and cross-check sources, not sole authority for low-level technical claims.
- Forum research is retained with author/date/thread context and should be reproduced against source/data where possible.
- ROM/distribution binaries are not committed. Record hashes, product codes, provenance, structure and derived analysis instead.
- Unauthorized proprietary source leaks are not imported into this repository. If their existence becomes relevant to provenance history, record only safe bibliographic metadata and independently verifiable conclusions.

## Search-log requirement

Every research batch should record:

- date checked
- source family
- search service/site
- Japanese query terms
- English/other-language query terms
- result URLs reviewed
- useful / duplicate / derivative / dead / inaccessible classification
- follow-up actions

A future machine-readable search/source manifest should mirror this document and permit deduplication by canonical URL, repository identity, artifact hash, or publication identity.