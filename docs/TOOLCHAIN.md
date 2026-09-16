# Sapphire decompilation toolchain

This repository targets **Pokémon Sapphire for the Game Boy Advance**, so the development environment is built around ARM7TDMI/GBA tooling rather than Game Boy RGBDS tooling.

## Core environment

The reproducible bootstrap entry point is:

```bash
tools/setup_gba_environment.sh install
source .local/env.sh
```

Local third-party binaries and source checkouts are installed under `.local/`, which is already excluded by `.gitignore`. Retail ROM images remain outside the repository.

### Required components

| Component | Role | Policy |
| --- | --- | --- |
| devkitARM / `gba-dev` | ARM7TDMI assembler, linker, objdump, GCC, GBA utilities | install through devkitPro; current package set |
| `pret/agbcc` | historical compiler used by Generation III matching decompilation work | pinned by the bootstrap script to commit `da598c1d918402c42c0c0d7128ba14567f3175e9` |
| GNU Make, Git, GCC/G++, Python 3 | host build and analysis tooling | host package manager |
| libpng + pkg-config | graphics conversion/build dependencies used by established Gen III decomp workflows | host package manager |
| mGBA | runtime/emulator verification, debugging and save/RTC testing | stable release `0.10.5` pinned by default |

`tools/check_gba_environment.py` verifies the core command set and reports optional GBA utilities when present.

## Emulator

mGBA is the primary emulator for this repository. The bootstrap downloads the official Linux AppImage into:

```text
.local/emulators/mgba/
```

and exposes it as:

```text
.local/bin/mgba
```

Launch it through:

```bash
tools/run_mgba.sh path/to/local-sapphire.gba
```

Do not place ROM images in Git. The wrapper accepts a local path only.

## devkitARM

On Debian/Ubuntu, the bootstrap uses devkitPro's official pacman setup script and installs the `gba-dev` package group. After installation, `.local/env.sh` exports `DEVKITPRO` and `DEVKITARM` and adds the devkitARM binaries to `PATH`.

The important commands for this project include:

- `arm-none-eabi-as`
- `arm-none-eabi-ld`
- `arm-none-eabi-objdump`
- `arm-none-eabi-objcopy`
- `arm-none-eabi-gcc`
- `arm-none-eabi-gdb` when supplied by the installed toolchain
- GBA utilities such as `gbafix` and `grit` when supplied by `gba-dev`

## agbcc

The bootstrap clones `pret/agbcc` into `.local/src/agbcc`, checks out the pinned commit, builds it, and installs it under `.local/agbcc-sdk/tools/agbcc`.

This compiler is retained because established Generation III Pokémon decompilation projects use agbcc for matching original retail code, while devkitARM's GCC remains useful for modern/nonmatching development and tooling.

## Optional static-analysis workstation

Ghidra is recommended for interactive static analysis but is not a build dependency. As of 2026-09-16 the current official release is **Ghidra 12.1.3**, whose official installation instructions require a **64-bit JDK 25**. Keep Ghidra itself outside version control, for example under `.local/tools/ghidra`, and commit only project-created analysis notes or scripts that follow this repository's provenance rules.

## Session environments

Chat/runtime sessions may not permit outbound package downloads. The repository therefore stores the bootstrap and checker rather than third-party binaries. When downloads are permitted, run the bootstrap once; on later sessions, source `.local/env.sh` and run the checker.

If a restricted session already provides Clang/LLVM, those tools may be used for exploratory ARM/Thumb assembly and disassembly, but they do **not** replace the pinned matching toolchain recorded here.
