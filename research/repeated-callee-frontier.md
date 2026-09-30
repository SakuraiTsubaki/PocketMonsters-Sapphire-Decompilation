# Repeated bootstrap callee frontier

The AXPJ revision 0 bootstrap calls `0x08000348` three times. A publication-safe
Thumb trace reaches the return at `0x080003e2`, covers 78 instruction positions,
records seven direct call sites and eight branch edges, and omits raw ROM
halfwords. This is the next behavior-reconstruction frontier.
