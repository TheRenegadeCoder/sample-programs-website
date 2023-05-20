---
title: Hello World in X86 64
layout: default
date: 2023-05-04
featured-image: hello-world-in-every-language.jpg
last-modified: 2023-05-04

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [X86 64](https://sampleprograms.io/languages/x86-64) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```x86_64
section .rodata
    message db 'Hello, World!'
    message_len equ $-message

section .text
    global _start

_start:
    ; write message to stdout
    mov rax, 1 ; 1 is the system call number for write
    mov rdi, 1 ; 1 is the file descriptor for stdout
    mov rsi, message ; address of the message to print
    mov rdx, message_len ; number of bytes to print
    syscall ; invoke the system call

    ; exit program with 0
    mov rax, 60 ; 60 is the system call number for exit
    xor rdi, rdi ; the exit status is stored in rdi. Use xor to zero it out
    syscall ; invoke the system call
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [X86 64](https://sampleprograms.io/languages/x86-64) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).