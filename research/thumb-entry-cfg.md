# Thumb entry reachable control flow

Exact-hash analysis starts at the proven Thumb target `0x0800024c`. Conservative traversal reaches 107 halfwords across `0x0800024c`–`0x08000344`, records 18 direct edges and 21 BL calls, and does not follow callees. No return is reachable in this graph; this is evidence for a non-returning bootstrap path, not a claimed complete function boundary. The scan ceiling is `0x0800424c`.

