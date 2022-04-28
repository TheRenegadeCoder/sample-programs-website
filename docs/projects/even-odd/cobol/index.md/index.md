# Even Odd in Cobol

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Cobol
        IDENTIFICATION DIVISION.
        PROGRAM-ID. HELLO-WORLD.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
          01 CMDARGS PIC X(38).
          01 NUM     PIC S9(30).
        PROCEDURE DIVISION.
           ACCEPT CMDARGS FROM COMMAND-LINE.
           IF CMDARGS IS ALPHABETIC THEN
              DISPLAY "Usage: please input a number"
              STOP RUN.
           COMPUTE NUM = FUNCTION NUMVAL(CMDARGS).
           IF NUM IS NUMERIC THEN
              IF FUNCTION MOD (NUM, 2) = 0 THEN
                 DISPLAY "Even"
              ELSE
                 DISPLAY "Odd"
           ELSE 
              DISPLAY "Usage: please input a number"
           STOP RUN.

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.