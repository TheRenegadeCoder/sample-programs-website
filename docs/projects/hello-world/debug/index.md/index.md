# Hello World in Debug

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Debug
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.