---

title: Prime Number in Cobol
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Prime Number in Cobol page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Cobol
        IDENTIFICATION DIVISION.
        PROGRAM-ID. HELLO-WORLD.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
          01 CMDARGS     PIC X(38).
          01 DECINUM     PIC S9999v99.
          01 NUM         PIC S9(7).
          01 SQRT        PIC 9(7).
          01 CNT         PIC 9(7) VALUE 3.
          01 PRIME       PIC 9(1) VALUE 0.
        PROCEDURE DIVISION.
           ACCEPT CMDARGS FROM COMMAND-LINE.

           IF CMDARGS IS ALPHABETIC THEN
              PERFORM ERROR-PARA.
           
      * Convert CMDARGS to it's cumeric value
           COMPUTE DECINUM = FUNCTION NUMVAL(CMDARGS).
           
           IF DECINUM < 0 THEN
              PERFORM ERROR-PARA.

      * Move the Decimal number to Non decimal number
           MOVE DECINUM TO NUM
      
      * If both are equal, then it was an integer
           IF NUM IS EQUAL TO DECINUM THEN
              IF FUNCTION MOD (NUM, 2) = 0 AND NUM IS NOT EQUAL TO 2
                 PERFORM DISPLAY-COMPOSITE
              ELSE IF NUM IS EQUAL TO 1
                 PERFORM DISPLAY-COMPOSITE
              ELSE
                 COMPUTE SQRT = NUM ** 0.5
                 PERFORM ISPRIME UNTIL CNT > SQRT
                 DISPLAY "Prime"
                 STOP RUN
           ELSE 
              PERFORM ERROR-PARA.
           
           
          ISPRIME.
            IF FUNCTION MOD (NUM, CNT) = 0 THEN
               PERFORM DISPLAY-COMPOSITE
            ELSE
               COMPUTE CNT = CNT + 1
            END-IF.
           
          DISPLAY-COMPOSITE.
            DISPLAY "Composite"
            STOP RUN.

          ERROR-PARA.
           DISPLAY "Usage: please input a non-negative integer".
           STOP RUN.

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.