---
title: Fizz Buzz in X86 64
layout: default
date: 2023-05-05
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-05-05

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [X86 64](https://sampleprograms.io/languages/x86-64) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```x86_64
section .data
    fizz db "Fizz"
    fizz_len equ $-fizz
    buzz db "Buzz"
    buzz_len equ $-buzz
    newline db 10

section .bss
    ; Used to hold the ascii digits for printing
    ; Sufficient size to hold any positive 64 bit number
    digits resb 21 

section .text
    global _start

_start:
    mov r12, 1    ; r12 holds current i
    mov r13, 101  ; r13 holds loop end (exclusive)

    loop:
        ; Break loop once target reached
        cmp r12, r13
        je loop_end

        mov rax, r12
        call print_val

        ; Print a newline character
        mov rax, 1
        mov rdi, 1
        mov rsi, newline
        mov rdx, 1
        syscall

        inc r12
        jmp loop

    loop_end:
        ; Exit and return 0
        mov rax, 60
        xor rdi, rdi
        syscall


; Prints an int. Currently only works for positive values
; rax holds input number
print_num:
    mov r8, 20 ; r8 holds the offset from the digits buffer. We start at the back
    mov r9, 10 ; We will be repeatedly dividing by 10

    div_loop:
        ; Calculate ASCII value of last decimal digit of rax
        xor rdx, rdx
        div r9
        add rdx, '0'

        ; Fill ASCII values from the end of the buffer
        mov byte [digits + r8], dl
        dec r8
        cmp rax, 0
        jne div_loop

    ; Move r8 offest to start of string
    inc r8

    ; Print the string
    mov rax, 1
    mov rdi, 1
    lea rsi, [digits + r8]
    mov rdx, 21
    sub rdx, r8
    syscall

    ret

    
print_val:
    push r12
    push r13

    xor r12, r12 ; Flag as to whether fizz || buzz was printed
    mov r13, rax ;  Keep a copy of the input to re-use
    
    test_fizz:
        ; Skip to next label if not divisible by 3
        xor rdx, rdx
        mov r8, 3
        div r8
        cmp rdx, 0
        jne test_buzz

        ; Print Fizz
        mov rax, 1
        mov rdi, 1
        mov rsi, fizz
        mov rdx, fizz_len
        syscall

        ; Mark that a wword was printed for this number
        inc r12     

    test_buzz:
        ; Restore the input value to rax
        mov rax, r13

        ; Skip to the next label if not divisible by 5
        xor rdx, rdx
        mov r8, 5
        div r8
        cmp rdx, 0
        jne test_num

        ; Print Buzz
        mov rax, 1
        mov rdi, 1
        mov rsi, buzz
        mov rdx, buzz_len
        syscall

        ; Mark that a wword was printed for this number
        inc r12 

    test_num:
        ; If fizz and/or buzz was already printed for this number, skip to cleanup
        cmp r12, 0
        jne cleanup

        ; Restore the input to rax and print it
        mov rax, r13
        call print_num

    cleanup:
        pop r13
        pop r12
        ret
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [X86 64](https://sampleprograms.io/languages/x86-64) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).