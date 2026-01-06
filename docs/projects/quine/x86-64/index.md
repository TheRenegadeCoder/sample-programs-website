---
authors:
- Raymond Marx
date: 2026-01-06
featured-image: quine-in-every-language.jpg
last-modified: 2026-01-06
layout: default
tags:
- quine
- x86-64
title: Quine in X86 64
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/x86-64/how-to-implement-the-solution.md
- sources/programs/quine/x86-64/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [X86 64](https://sampleprograms.io/languages/x86-64) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```x86_64
; SYSCALLS
%DEFINE SYS_READ 0
%DEFINE SYS_WRITE 1
%DEFINE STDOUT 1
%DEFINE SYS_EXIT 60
section .data
string:
.msg db "; SYSCALLS%DEFINE SYS_READ 0%DEFINE SYS_WRITE 1%DEFINE STDOUT 1%DEFINE SYS_EXIT 60section .datastring:.msg db .len equ $- .msgquote db 0x22newline db 0xAlinestarts dw 0, 10, 18, 19, 16, 19, 13, 7, 8linestarts2 dw 16, 13, 14, 45, 312, 17, 13, 13, 7, 19, 10, 11, 12, 6, 12, 18, 15, 12, 31, 24, 7, 12, 12, 8, 18, 15, 16, 10, 7, 12, 10, 12, 9, 6, 18, 15, 14, 10, 7, 18, 15, 19, 19, 7, 18, 15, 14, 10, 7, 18, 15, 16, 10, 7, 10, 6, 12, 18, 15, 12, 32, 25, 7, 12, 12, 8, 18, 15, 16, 10, 7, 12, 10, 12, 9, 6, 11, 10, 7%DEFINE PRINT1 90section .textglobal _start_start:MOV R12, string.msgMOV R13, 2MOV R14, 16MOV R15, 158loop0:MOV RCX, R13MOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, R12ADD R12W, WORD [linestarts+RCX]MOV DX, [linestarts+RCX]SYSCALLMOV RCX, R13CMP RCX, R14JE exit1MOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, newlineMOV RDX, 1SYSCALLMOV RCX, R13ADD RCX, 2MOV R13, RCXJMP loop0exit1:MOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, quoteMOV RDX, 1SYSCALLMOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, string.msgMOV RDX, string.lenSYSCALLMOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, quoteMOV RDX, 1SYSCALLMOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, newlineMOV RDX, 1SYSCALLMOV R13, 0loop1:MOV RCX, R13MOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, R12ADD R12W, WORD [linestarts2+RCX]MOV DX, [linestarts2+RCX]SYSCALLMOV RCX, R13CMP RCX, R15JE exit2MOV RAX, SYS_WRITEMOV RDI, STDOUTMOV RSI, newlineMOV RDX, 1SYSCALLMOV RCX, R13ADD RCX, 2MOV R13, RCXJMP loop1exit2:MOV RAX, 60MOV RDI, 0SYSCALL"
.len equ $- .msg
quote db 0x22
newline db 0xA
linestarts dw 0, 10, 18, 19, 16, 19, 13, 7, 8
linestarts2 dw 16, 13, 14, 45, 312, 17, 13, 13, 7, 19, 10, 11, 12, 6, 12, 18, 15, 12, 31, 24, 7, 12, 12, 8, 18, 15, 16, 10, 7, 12, 10, 12, 9, 6, 18, 15, 14, 10, 7, 18, 15, 19, 19, 7, 18, 15, 14, 10, 7, 18, 15, 16, 10, 7, 10, 6, 12, 18, 15, 12, 32, 25, 7, 12, 12, 8, 18, 15, 16, 10, 7, 12, 10, 12, 9, 6, 11, 10, 7
%DEFINE PRINT1 90
section .text
global _start
_start:
MOV R12, string.msg
MOV R13, 2
MOV R14, 16
MOV R15, 158
loop0:
MOV RCX, R13
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, R12
ADD R12W, WORD [linestarts+RCX]
MOV DX, [linestarts+RCX]
SYSCALL
MOV RCX, R13
CMP RCX, R14
JE exit1
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, newline
MOV RDX, 1
SYSCALL
MOV RCX, R13
ADD RCX, 2
MOV R13, RCX
JMP loop0
exit1:
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, quote
MOV RDX, 1
SYSCALL
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, string.msg
MOV RDX, string.len
SYSCALL
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, quote
MOV RDX, 1
SYSCALL
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, newline
MOV RDX, 1
SYSCALL
MOV R13, 0
loop1:
MOV RCX, R13
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, R12
ADD R12W, WORD [linestarts2+RCX]
MOV DX, [linestarts2+RCX]
SYSCALL
MOV RCX, R13
CMP RCX, R15
JE exit2
MOV RAX, SYS_WRITE
MOV RDI, STDOUT
MOV RSI, newline
MOV RDX, 1
SYSCALL
MOV RCX, R13
ADD RCX, 2
MOV R13, RCX
JMP loop1
exit2:
MOV RAX, 60
MOV RDI, 0
SYSCALL

```

{% endraw %}

Quine in [X86 64](https://sampleprograms.io/languages/x86-64) was written by:

- Raymond Marx

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).