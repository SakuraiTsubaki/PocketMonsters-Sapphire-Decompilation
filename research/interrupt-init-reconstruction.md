# AXPJ revision 0 interrupt initialization

`InitIntrHandlers` at `0x080004C8` copies 14 interrupt callbacks, copies
`IntrMain` to the 0x800-byte IWRAM buffer with DMA3, installs the interrupt
vector, clears the VBlank/HBlank/Serial callbacks, and enables VBlank IRQ state.

The four callback setters at `0x08000544` through `0x08000573` prove the
`gMain` callback offsets. The Sapphire interrupt table template is
`0x081B325C`; this game-specific literal is not substituted from the other
version. Exact ROM-range and output hashes are retained without publishing raw
instruction bytes.
