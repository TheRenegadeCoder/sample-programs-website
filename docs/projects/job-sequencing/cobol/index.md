---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-05
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- cobol
- job-sequencing
title: Job Sequencing in COBOL
title1: Job Sequencing
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/cobol/how-to-implement-the-solution.md
- sources/programs/job-sequencing/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. job-sequencing.

data division.
working-storage section.

01 ws-inputs.
   05 ws-profits-line     pic x(200).
   05 ws-deadlines-line   pic x(200).
   05 ws-temp             pic x(200).

01 ws-counters.
   05 ws-profit-count     pic 9(4) value 0.
   05 ws-deadline-count   pic 9(4) value 0.
   05 ws-job-count        pic 9(4) value 0.
   05 ws-max-deadline     pic 9(4) value 0.
   05 ws-pos              pic 9(4).

01 ws-indices.
   05 ws-i                pic 9(4).
   05 ws-j                pic 9(4).
   05 ws-x                pic 9(4).
   05 ws-y                pic 9(4).

01 ws-logic-vars.
   05 ws-max-profit       pic 9(12) value 0.
   05 ws-profit-temp      pic 9(9).
   05 ws-deadline-temp    pic 9(9).
   05 ws-find-result      pic 9(4).
   05 ws-next             pic 9(4).

01 ws-flags.
   05 ws-valid-flag       pic x value "y".
      88 is-valid         value "y".
      88 is-invalid       value "n".

01 ws-jobs-table.
   05 job occurs 1 to 50 times 
          depending on ws-job-count
          descending key is job-profit.
      10 job-profit    pic 9(9).
      10 job-deadline  pic 9(9).

01 ws-dsu-table.
   05 parent occurs 51 times pic 9(4).

01 ws-display.
   05 ws-out              pic -(11)9.

procedure division.

main.
    accept ws-profits-line from argument-value
    accept ws-deadlines-line from argument-value

    if ws-profits-line = spaces or ws-deadlines-line = spaces
        perform show-usage
        stop run
    end-if

    perform parse-input

    if is-invalid
        perform show-usage
        stop run
    end-if

    sort job on descending key job-profit.

    perform schedule-jobs-dsu

    move ws-max-profit to ws-out
    display function trim(ws-out)
    stop run.


parse-input.
    set is-valid to true
    
    move 1 to ws-pos
    perform until ws-pos > length of ws-profits-line
        unstring ws-profits-line delimited by ","
            into ws-profit-temp
            with pointer ws-pos
        end-unstring
        
        if ws-profit-temp not = spaces
            add 1 to ws-profit-count
            if ws-profit-count <= 50
                move ws-profit-temp to job-profit(ws-profit-count)
            end-if
        end-if
    end-perform

    move 1 to ws-pos
    perform until ws-pos > length of ws-deadlines-line
        unstring ws-deadlines-line delimited by ","
            into ws-deadline-temp
            with pointer ws-pos
        end-unstring

        if ws-deadline-temp not = spaces
            add 1 to ws-deadline-count
            if ws-deadline-count <= 50 and <= ws-profit-count
                move ws-deadline-temp to job-deadline(ws-deadline-count)
                if job-deadline(ws-deadline-count) > ws-max-deadline
                    move job-deadline(ws-deadline-count) to ws-max-deadline
                end-if
            end-if
        end-if
    end-perform

    if ws-profit-count not = ws-deadline-count or ws-profit-count = 0
        set is-invalid to true
    else
        move ws-profit-count to ws-job-count
    end-if.

schedule-jobs-dsu.
    perform varying ws-i from 0 by 1 until ws-i > ws-max-deadline
        move ws-i to parent(ws-i + 1)
    end-perform

    move 0 to ws-max-profit
    perform varying ws-i from 1 by 1 until ws-i > ws-job-count
        move job-deadline(ws-i) to ws-x
        
        move ws-x to ws-y
        perform until parent(ws-y + 1) = ws-y
            move parent(ws-y + 1) to ws-y
        end-perform
        move ws-y to ws-find-result
        
        if ws-find-result > 0
            add job-profit(ws-i) to ws-max-profit
            compute ws-next = ws-find-result - 1
            move parent(ws-next + 1) to parent(ws-find-result + 1)
        end-if
    end-perform.

show-usage.
    display "Usage: please provide a list of profits and a list of deadlines".
```

{% endraw %}

Job Sequencing in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).