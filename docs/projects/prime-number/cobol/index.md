---
title: Prime Number in Cobol
layout: default
date: 2021-10-12
featured-image: prime-number-in-every-language.jpg
last-modified: 2021-10-12

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Cobol](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
        IDENTIFICATION DIVISION.
        PROGRAM-ID. PRIME-NUMBER.
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

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Cobol](https://sampleprograms.io/languages/cobol) was written by:

- Ron Zuckerman
- Sudhanshu Dubey

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:11:58. The solution was first committed on Oct 12 2021 18:48:29. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).