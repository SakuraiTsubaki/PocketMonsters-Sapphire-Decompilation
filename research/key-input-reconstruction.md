# AXPJ revision 0 key-input reconstruction

The Japanese Sapphire `InitKeys` (`0x08000404`) and `ReadKeys`
(`0x0800042C`) range has SHA-256
`6f57c651796485bd14d6e53f08bed93660ec1b6496557070b7c643211a8ec0ba`.
It is byte-identical to the independently selected Japanese Ruby range, but
this project records the AXPJ ROM identity and evidence separately.

The functions implement key initialization, repeat timing, active-low keypad
input, L-to-A option remapping, and the watched-key latch. Exact addresses,
structure offsets, and literals are preserved in the map without publishing
ROM instruction bytes.
