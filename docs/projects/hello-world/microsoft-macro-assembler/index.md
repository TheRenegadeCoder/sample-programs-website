---
title: Hello World in Microsoft Macro Assembler
layout: default
date: 2020-04-23
featured-image: hello-world-in-every-language.jpg
last-modified: 2020-04-23

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Microsoft Macro Assembler](https://sampleprograms.io/languages/microsoft-macro-assembler) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```microsoft_macro_assembler
PAGE 60,132
;
.8086
XSEG SEGMENT
 ASSUME CS:XSEG

START: PUSH DS
 PUSH DI
 PUSH CS
 POP DS
 PUSH AX
 PUSH DX
 MOV AX,0003H
 MOV AH,09H
 LEA DX,STR   ; Address of string relative to start of code
 ADD DX,100H  ; *****
 INT 21H      ; Print string

EXIT: POP DX
 POP AX
 POP DI
 POP DS
 RET
 
STR: DB 'Hello world!',0DH,0AH,'$'
 DB 103 DUP(0)

XSEG ENDS
 END
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Microsoft Macro Assembler](https://sampleprograms.io/languages/microsoft-macro-assembler) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).