# Version Coverage

Use this document as the authoritative human-readable inventory of game versions targeted by this decompilation project. The machine-readable record is `../manifests/version-inventory.json`.

| Status | Target ID | Game code | Region / language | Revision | Size | SHA-256 |
| --- | --- | --- | --- | ---: | ---: | --- |
| Verified | `sapphire-axpd-rev1-de` | AXPD | Germany / German | 1 | 16 MiB | `c27271a60fdeadc6eed957e0392e7d878998ae1765487bf7567fa9331e432ead` |
| Verified | `sapphire-axpi-rev1-it` | AXPI | Italy / Italian | 1 | 16 MiB | `e2f75b0ce7c55d5cbe6ec23eee5f2806101a02a00a13b3c4fdfe7f7d3e8b6898` |
| Verified | `sapphire-axpj-rev0-ja` | AXPJ | Japan / Japanese | 0 | 8 MiB | `6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9` |
| Verified | `sapphire-axpe-rev1-en-eu` | AXPE | Europe / English | 1 | 16 MiB | `2f680a43e5c57aede4cb3b2cb04f7e15079efc122c88edaacfd6026db6e920ac` |
| Verified | `sapphire-axpf-rev0-fr` | AXPF | France / French | 0 | 16 MiB | `687dcb560ad4ecec719c9ee94b5a58bde3185d5afbceaf8560b6b907a493f92e` |
| Verified | `sapphire-axpi-rev0-it` | AXPI | Italy / Italian | 0 | 16 MiB | `74795c4301e02121d2687e0d1b89335534dae1a18af72e022725589f28c97fe0` |
| Verified | `sapphire-axpe-rev2-en-us-eu` | AXPE | USA/Europe / English | 2 | 16 MiB | `02ca41513580a8b780989dee428df747b52a0b1a55bec617886b4059eb1152fb` |
| Verified | `sapphire-axpe-rev0-en-us` | AXPE | USA / English | 0 | 16 MiB | `c36c1b899503e8823ee7eb607eea583adcef7ea92ff804838b193c227f2c6657` |
| Verified | `sapphire-axpf-rev1-fr` | AXPF | France / French | 1 | 16 MiB | `476ef6e6534894d0646265a4db77fff84b10f04fde81f0730dd07b28f086fb04` |

## Current mapping notes

- All nine target headers pass the GBA header complement check.
- AXPJ revision 0 is the only observed 8 MiB target; the other eight are 16 MiB.
- Current Phase 1 layout evidence is stored in `../manifests/binary-baseline.json`, `../manifests/revision-differences.json`, and `../manifests/executable-map.json`.
- AXPE revision 0 differs broadly from AXPE revisions 1 and 2; it is not treated as merely the same layout plus the small revision fix observed between AXPE rev1 and rev2.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes confirmed.
- **Mapped** — executable/data layout documented to the defined mapping criterion.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to the relevant documentation or verification record.
6. Do not promote a target from **Verified** to **Mapped** until the mapping criterion is documented and satisfied.
