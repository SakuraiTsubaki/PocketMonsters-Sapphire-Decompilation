# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

## Baseline policy

This project uses the original Japanese release as the historical baseline and traces every confirmed regional, language, and revision branch from that point. Later regional releases remain separate targets when code, data, text, graphics, events, fixes, product identity, or distribution context differs.

The project does not currently assume access to a retail ROM image. Version identities are established from public documentation, hardware/cartridge databases, public reverse-engineering repositories, hashes, and reproducible evidence.

## Japanese baseline

| Status | Region | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | Japan | Japanese | Rev 0 / v1.0 | GBA / AGB-AXPJ-0 / retail code AGB-AXPJ-JPN | SHA-1 `3233342c2f3087e6ffe6c1791cd5867db07df842` | Historical baseline. Official Japanese release date: 2002-11-21. |
| Verified | Japan | Japanese | Rev 1 / v1.1 | GBA / AGB-AXPJ-1 | SHA-1 `01f509671445965236ac4c6b5a354fe2f1e69f13` | Confirmed Japanese revision. Exact binary delta remains a separate verification task. |

See [`versions/JAPANESE_BASELINE.md`](versions/JAPANESE_BASELINE.md) for evidence and provenance.

## Confirmed regional/revision branches — first-pass inventory

| Status | Region / market | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | North America | English | Rev 0 | GBA / AGB-AXPE-0 / retail code AGB-AXPE-USA | SHA-1 `3ccbbd45f8553c36463f13b938e833f652b793e4` | Public `pret/pokeruby` default matching target for Sapphire. |
| Verified | North America branch | English | Rev 1 | GBA / AGB-AXPE-1 | TBD | Variant existence confirmed; exact hash/product mapping still being cross-verified. |
| Verified | North America branch | English | Rev 2 | GBA / AGB-AXPE-2 | TBD | Variant existence confirmed; exact hash/product mapping still being cross-verified. |
| Verified | Europe / Australia English distribution | English | Rev 0 | GBA / AGB-AXPP-0 / retail codes include AGB-AXPP-EUR and AGB-AXPP-AUS | TBD | Market identity and binary identity tracked separately. |
| Verified | Europe / Australia English distribution | English | Rev 1 | GBA / AGB-AXPP-1 | TBD | Exact region/hash mapping pending. |
| Verified | Europe / Australia English distribution | English | Rev 2 | GBA / AGB-AXPP-2 | TBD | Exact region/hash mapping pending. |
| Verified | Germany | German | Rev 0 | GBA / AGB-AXPD-0 | SHA-1 `5a087835009d552d4c5c1f96be3be3206e378153` | Public hash inventory; `pret/pokeruby` supports German builds. |
| Verified | Germany | German | Rev 1 | GBA / AGB-AXPD-1 | SHA-1 `7e6e034f9cdca6d2c4a270fdb50a94def5883d17` | Public hash inventory. |
| Verified | France | French | Rev 0 | GBA / AGB-AXPF-0 | SHA-1 `c269b5692b2d0e5800ba1ddf117fda95ac648634` | Public hash inventory. |
| Verified | France | French | Rev 1 | GBA / AGB-AXPF-1 | SHA-1 `860e93f5ea44f4278132f6c1ee5650d07b852fd8` | Public hash inventory. |
| Verified | Italy | Italian | Rev 0 | GBA / AGB-AXPI-0 | SHA-1 `f729dd571fb2c09e72c5c1d68fe0a21e72713d34` | Public hash inventory. |
| Verified | Italy | Italian | Rev 1 | GBA / AGB-AXPI-1 | SHA-1 `73edf67b9b82ff12795622dca412733755d2c0fe` | Public hash inventory. |
| Verified | Spain | Spanish | Rev 0 | GBA / AGB-AXPS-0 | SHA-1 `3a6489189e581c4b29914071b79207883b8c16d8` | Public hash inventory. |
| Verified | Spain | Spanish | Rev 1 | GBA / AGB-AXPS-1 | SHA-1 `0fe9ad1e602e2fafa090aee25e43d6980625173c` | Public hash inventory. |

## Public reconstruction coverage

`pret/pokeruby` is an important public Ruby/Sapphire reconstruction reference, but its current configuration exposes only English and German language targets and revisions 0-2. Japanese, French, Italian, and Spanish reconstruction therefore remain independent research/reconstruction targets for this repository unless additional verified public sources are found.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes or stable build identifiers confirmed from recorded public evidence.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to the relevant documentation or verification issue.
6. Treat the Japanese release as the comparison baseline while preserving all later regional branch history.
7. Keep market/packaging identity separate from binary identity where one language is distributed under multiple market codes.
8. Use `TBD` or `unknown` instead of guessing unresolved mappings.
