.syntax unified
.thumb

.global VBlankIntrWait
.type VBlankIntrWait, %function
VBlankIntrWait:
    movs r2, #0
    swi 5
    bx lr
.size VBlankIntrWait, . - VBlankIntrWait
