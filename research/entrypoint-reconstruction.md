# Japanese ROM entrypoint reconstruction

The selected Japanese target begins with ARM word `0xea000032`, branching from `0x08000000` to `0x080000d0` under ARM PC+8 semantics. The checked-in assembly preserves the exact word and the JSON evidence is gated by the selected target SHA-256. No ROM binary is stored.
