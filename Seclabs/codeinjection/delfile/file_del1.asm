; delete dummyfile in nasm

section .text
global _start
_start:
    jmp short ender
starter:
    xor eax, eax
    mov al, 5
    add al, 5
    mov ebx,_filename
    int 0x80
_exit:
    xor eax, eax
    mov al, 2
    sub al, 1
    int 0x80

ender:
    call starter
_filename:
    db 'dummyfile'