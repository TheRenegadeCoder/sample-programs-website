---
title: Factorial in Cobol
layout: default
date: 2021-10-14
featured-image: factorial-in-every-language.jpg
last-modified: 2021-10-14

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Cobol](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
        IDENTIFICATION DIVISION.
        PROGRAM-ID. FACTORIAL.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
          01 CMD-ARGS                  PIC X(38).
          01 DECINUM                  PIC S9999v99.
          01 NUM                      PIC S9(7).
          01 FACTORIAL                PIC 9(15) VALUE 1.
          01 LEFT-JUST-NUMBER         PIC X(16).
          01 WS-TALLY1                PIC 99 VALUE 0.
          01 CNT                      PIC 9(7) VALUE 1.

        PROCEDURE DIVISION.
           ACCEPT CMD-ARGS FROM COMMAND-LINE.

           IF CMD-ARGS IS ALPHABETIC THEN
              PERFORM ERROR-PARA.
           
      * Convert CMDARGS to it's numeric value
           COMPUTE DECINUM = FUNCTION NUMVAL(CMD-ARGS).
           
           IF DECINUM < 0 THEN
              PERFORM ERROR-PARA.

      * Move the Decimal number to Non decimal number
           MOVE DECINUM TO NUM
      
      * If both are equal, then it was an integer
           IF NUM IS EQUAL TO DECINUM THEN
              IF NUM IS EQUAL TO 0 OR NUM IS EQUAL TO 1 THEN
                 DISPLAY 1
                 STOP RUN                 
              ELSE
                 PERFORM CALC-FACT UNTIL CNT > NUM
      
      * Process to left justify the number
                 INSPECT FACTORIAL TALLYING WS-TALLY1 FOR LEADING ZEROS
                 Move FACTORIAL (WS-TALLY1 + 1 :) TO LEFT-JUST-NUMBER
      * Display the left justified result
                 DISPLAY LEFT-JUST-NUMBER
                 STOP RUN
           ELSE 
              PERFORM ERROR-PARA.
           
           
          CALC-FACT.
            COMPUTE FACTORIAL = FACTORIAL * CNT
            COMPUTE CNT = CNT + 1.

          ERROR-PARA.
           DISPLAY "Usage: please input a non-negative integer".
           STOP RUN.
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Cobol](https://sampleprograms.io/languages/cobol) was written by:

- Sudhanshu Dubey

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).