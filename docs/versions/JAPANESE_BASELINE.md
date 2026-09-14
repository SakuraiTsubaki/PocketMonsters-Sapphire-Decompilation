# Japanese Baseline — Pokémon Sapphire

This document records the current evidence for the Japanese release that serves as the historical baseline for the Sapphire decompilation project.

## Baseline rule

The Japanese release is the comparison origin for regional research. Later regional releases are preserved as separate branch history whenever fixes, content, localization, assets, events, product identity, or distribution context differs.

No retail ROM image is required or committed by this repository. Identity and reconstruction work begins from public evidence, reverse-engineering material, hashes, hardware metadata, and reproducible analysis.

## Confirmed identity

| Field | Rev 0 / v1.0 | Rev 1 / v1.1 |
| --- | --- | --- |
| Title | ポケットモンスター サファイア | ポケットモンスター サファイア |
| Platform | Game Boy Advance | Game Boy Advance |
| Market | Japan | Japan |
| Language | Japanese | Japanese |
| Product/build identifier | AGB-AXPJ-0 | AGB-AXPJ-1 |
| Retail product code | AGB-AXPJ-JPN | AGB-AXPJ-JPN revision branch |
| SHA-1 | `3233342c2f3087e6ffe6c1791cd5867db07df842` | `01f509671445965236ac4c6b5a354fe2f1e69f13` |
| Repository role | Primary historical baseline | Japanese revision branch |

## Official release context

The Pokémon Company official Japanese product page records Ruby and Sapphire as Game Boy Advance titles released in Japan on **2002-11-21**.

Official source:

- https://www.pokemon.co.jp/game/gba/rs/

## Physical-cartridge / revision evidence

The Game Boy hardware database records Japanese Sapphire as `AGB-AXPJ-JPN` and exposes separate No-Intro-linked variant identities for:

- `AGB-AXPJ-0` — Pocket Monsters - Sapphire (Japan)
- `AGB-AXPJ-1` — Pocket Monsters - Sapphire (Japan) (Rev 1)

A physical Rev 0 cartridge entry records an `AGB-E05-01` board and RTC hardware. The database also contains a photographed Rev 1 Japanese cartridge entry.

Sources:

- https://gbhwdb.gekkio.fi/cartridges/AGB-AXPJ-0/
- https://gbhwdb.gekkio.fi/cartridges/contributors/fexcollects.html

## Hash evidence

Current SHA-1 values are recorded from public ROM-identification/reverse-engineering references rather than a locally owned ROM:

- Rev 0: `3233342c2f3087e6ffe6c1791cd5867db07df842`
- Rev 1: `01f509671445965236ac4c6b5a354fe2f1e69f13`

Primary public reference used in this first pass:

- https://github.com/40Cakes/pokebot-gen3/blob/main/modules/roms.py

The Rev 1 SHA-1 is also independently reported in public Berry-glitch reverse-engineering discussion:

- https://archives.glitchcity.info/forums/board-109/thread-7192/

## Revision-difference research status

Public reverse-engineering research associates Japanese v1.1 with the Berry/RTC date-conversion fix and reports a very small byte-level change from v1.0.

This remains external research evidence until this repository reproduces the exact Sapphire Rev 0 ↔ Rev 1 source/function/offset delta from public material. Do not silently treat the external report as a `Matched` repository result.

## Public reconstruction coverage gap

`pret/pokeruby` covers Ruby and Sapphire but its current `config.mk` exposes only `ENGLISH` and `GERMAN` language targets, with revisions 0-2.

Therefore Japanese Sapphire cannot simply be declared matched to the public upstream. Shared engine structure may be used as a comparison reference, but Japanese-specific source, data, text, event, graphics, audio, and binary differences must be investigated explicitly.

Sources:

- https://github.com/pret/pokeruby
- https://github.com/pret/pokeruby/blob/master/config.mk

## Evidence classification

| Finding | Level | Reason |
| --- | --- | --- |
| Japanese release date 2002-11-21 | Observed | Official Japanese Pokémon site |
| `AGB-AXPJ-0` and `AGB-AXPJ-1` existence | Observed | Public hardware/No-Intro-linked cartridge evidence |
| Rev 0 and Rev 1 SHA-1 values | Observed / cross-referenced | Public ROM-identification sources |
| Exact Rev 0 ↔ Rev 1 byte delta | Hypothesis / external research evidence | Not yet reproduced inside this repository |
| Japanese matching decompilation | Not yet reproduced | Current public `pret/pokeruby` configuration does not expose Japanese |

## Next tasks

1. Cross-check Japanese Rev 0 and Rev 1 CRC32/MD5/SHA-1 identities against additional catalogued sources.
2. Reconstruct the Rev 0 ↔ Rev 1 change list and Berry/RTC fix at source/function level.
3. Inventory all public Japanese Sapphire source, symbol, map, script, text, graphics, audio, save, event, and communication research.
4. Compare each subsystem against public `pret/pokeruby` reconstruction without assuming byte identity.
5. Preserve Ruby/Sapphire shared-engine findings through references or manifests rather than duplicating identical project material without verification.
