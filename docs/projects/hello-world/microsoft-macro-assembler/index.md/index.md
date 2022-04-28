# Hello World in Microsoft Macro Assembler

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Microsoft Macro Assembler
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.