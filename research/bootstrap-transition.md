# Bootstrap ARM-to-Thumb transition

The Japanese target follows twelve ARM words from `0x080000d0` to `bx r1` at `0x080000fc`. A PC-relative load reads odd pointer `0x0800024d` from `0x08000244`, proving entry into Thumb code at `0x0800024c`.
