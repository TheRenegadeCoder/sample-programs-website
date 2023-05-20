---
title: Hello World in Debug
layout: default
date: 2020-10-09
featured-image: hello-world-in-every-language.jpg
last-modified: 2020-10-09

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Debug](https://sampleprograms.io/languages/debug) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```debug
; ------------------------------------------------------------------
; helloworld.asm
;
; This is a Win64 console program that writes "Hello World"
; on a single line and then exits.
;
; To assemble to .obj: nasm -f Win64 helloworld.asm
; To compile to .exe:  gcc helloworld.obj -o helloworld.exe
; ------------------------------------------------------------------

        global    _main                ; declare main() method
        extern    _printf              ; link to external library

        segment  .data
        message: db   'Hello world', 0xA, 0  ; text message
                    ; 0xA (10) is hex for (NL), carriage return
                    ; 0 terminates the line

        ; code is put in the .text section
        section .text
_main:                            ; the entry point! void main()
        push    message           ; save message to the stack
        call    _printf           ; display the first value on the stack
        add     esp, 4            ; clear the stack
        ret                       ; return
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Debug](https://sampleprograms.io/languages/debug) was written by:

- Subhasmita Swain

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).