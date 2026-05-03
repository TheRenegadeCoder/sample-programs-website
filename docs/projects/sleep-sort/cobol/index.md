---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-21
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-04-21
layout: default
tags:
- cobol
- sleep-sort
title: Sleep Sort in COBOL
title1: Sleep Sort
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/cobol/how-to-implement-the-solution.md
- sources/programs/sleep-sort/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. sleep-sort.

data division.
working-storage section.
01 argument-string      pic x(32768).
01 current-token        pic x(64).
01 scan-ptr             binary-long value 1.
01 temp-ptr             binary-long.

01 pipe-fds-table.
    05 pipe-read-fd     binary-long.
    05 pipe-write-fd    binary-long.

01 process-vars.
    05 pid              binary-long.
    05 child-val        binary-long.
    05 children-spawned binary-long value 0.
    05 children-done    binary-long value 0.

01 io-vars.
    05 write-buffer     pic x(32).
    05 pipe-buffer      pic x(128).
    05 formatted-val    pic -(10)9.
    05 bytes-read       binary-long.
    01 nl               pic x value x'0a'.

procedure division.
main.
    accept argument-string from command-line
    if argument-string = spaces perform show-usage.

    perform validate-input-count

    call "pipe" using pipe-fds-table returning pid
    if pid = -1 
        display "Error: Could not create pipe."
        stop run 1
    end-if
    
    perform spawn-sleepers

    call "close" using by value pipe-write-fd

    perform collect-results
    
    display space
    stop run.

validate-input-count.
    move 1 to temp-ptr
    move 0 to children-spawned
    perform until temp-ptr > function length(argument-string)
        move spaces to current-token
        unstring argument-string delimited by ","
            into current-token with pointer temp-ptr
        
        if function trim(current-token) not = spaces
            if function test-numval(function trim(current-token)) <> 0
                perform show-usage
            end-if
            add 1 to children-spawned
        end-if
    end-perform
    
    if children-spawned < 2 perform show-usage.

spawn-sleepers.
    move 1 to scan-ptr
    perform until scan-ptr > function length(argument-string)
        move spaces to current-token
        unstring argument-string delimited by ","
            into current-token with pointer scan-ptr
        
        if function trim(current-token) not = spaces
            move function numval(current-token) to child-val
            call "fork" returning pid
            
            evaluate true
                when pid = 0
                    call "close" using by value pipe-read-fd
                    
                    *> Wait for parent to finish loop
                    call "C$SLEEP" using 1
                    
                    if child-val < 0 move 0 to child-val end-if
                    call "C$SLEEP" using child-val
                    
                    move child-val to formatted-val
                    string function trim(formatted-val) nl 
                            delimited by size into write-buffer
                    
                    call "write" using by value pipe-write-fd
                                        by reference write-buffer
                                        by value function length(function trim(write-buffer))
                    call "exit" using by value 0
                
                when pid = -1
                    *> Fork failed (e.g. out of processes)
                    subtract 1 from children-spawned
            end-evaluate
        end-if
    end-perform.

collect-results.
    perform until children-done >= children-spawned
        move spaces to pipe-buffer
        call "read" using by value pipe-read-fd
                          by reference pipe-buffer
                          by value 128
                    returning bytes-read
        
        if bytes-read > 0
            perform parse-pipe-chunk
        else
            *> Pipe closed or error
            exit perform
        end-if
    end-perform.

parse-pipe-chunk.
    move 1 to temp-ptr
    perform until temp-ptr > bytes-read
        move spaces to current-token
        unstring pipe-buffer delimited by nl
            into current-token with pointer temp-ptr
        
        if current-token not = spaces
            add 1 to children-done
            display function trim(current-token) with no advancing
            
            if children-done < children-spawned
                display ", " with no advancing
            end-if
            call "fflush" using by value 0
        end-if
    end-perform.

show-usage.
    display 'Usage: please provide a list of at least two ' 
            'integers to sort in the format "1, 2, 3, 4, 5"'
    stop run 1.

```

{% endraw %}

Sleep Sort in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).