.syntax unified
.arm

/*
 * Reconstructed common ARM reset/IRQ path from observed Pokemon Sapphire ROMs.
 * This is source reconstruction, not copied ROM data.
 *
 * The reset/dispatcher code is structurally common across observed targets,
 * but the linked Thumb entry point and interrupt-table base are target-specific.
 */

.equ MODE_IRQ,             0x12
.equ MODE_SYSTEM,          0x1F
.equ IRQ_STACK_TOP,        0x03007FA0
.equ SYS_STACK_TOP,        0x03007E60
.equ BIOS_IRQ_VECTOR,      0x03007FFC

#ifndef SAPPHIRE_THUMB_ENTRY
#error "Define SAPPHIRE_THUMB_ENTRY for the selected target"
#endif

#ifndef SAPPHIRE_IRQ_TABLE
#error "Define SAPPHIRE_IRQ_TABLE for the selected target"
#endif

.section .text.boot, "ax", %progbits
.align 2
.global SapphireReset
.type SapphireReset, %function
SapphireReset:
    mov     r0, #MODE_IRQ
    msr     cpsr_fc, r0
    ldr     sp, =IRQ_STACK_TOP

    mov     r0, #MODE_SYSTEM
    msr     cpsr_fc, r0
    ldr     sp, =SYS_STACK_TOP

    ldr     r1, =BIOS_IRQ_VECTOR
    adr     r0, SapphireIrqDispatcher
    str     r0, [r1]

    ldr     r1, =SAPPHIRE_THUMB_ENTRY
    mov     lr, pc
    bx      r1

1:  b       SapphireReset
.size SapphireReset, . - SapphireReset

.align 2
.global SapphireIrqDispatcher
.type SapphireIrqDispatcher, %function
SapphireIrqDispatcher:
    mov     r3, #0x04000000
    add     r3, r3, #0x200
    ldr     r2, [r3]
    ldrh    r1, [r3, #8]
    mrs     r0, spsr
    push    {r0, r1, r2, r3, lr}

    mov     r0, #1
    strh    r0, [r3, #8]

    and     r1, r2, r2, lsr #16
    mov     r12, #0

    ands    r0, r1, #0x80
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x40
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x02
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x01
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x04
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x08
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x10
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x20
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x100
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x200
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x400
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x800
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x1000
    bne     2f
    add     r12, r12, #4
    ands    r0, r1, #0x2000
    strbne  r0, [r3, #-0x17C]
3:  bne     3b

2:  strh    r0, [r3, #2]
    mov     r1, #0xC2
    bic     r2, r2, r0
    and     r1, r1, r2
    strh    r1, [r3]

    mrs     r3, cpsr
    bic     r3, r3, #0xDF
    orr     r3, r3, #MODE_SYSTEM
    msr     cpsr_fc, r3

    ldr     r1, =SAPPHIRE_IRQ_TABLE
    add     r1, r1, r12
    ldr     r0, [r1]
    push    {lr}
    adr     lr, 4f
    bx      r0
4:  pop     {lr}

    mrs     r3, cpsr
    bic     r3, r3, #0xDF
    orr     r3, r3, #0x92
    msr     cpsr_fc, r3

    pop     {r0, r1, r2, r3, lr}
    strh    r2, [r3]
    strh    r1, [r3, #8]
    msr     spsr_fc, r0
    bx      lr
.size SapphireIrqDispatcher, . - SapphireIrqDispatcher
