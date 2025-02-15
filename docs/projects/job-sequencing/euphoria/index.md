---
authors:
- rzuckerm
date: 2023-02-27
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2023-02-27
layout: default
tags:
- euphoria
- job-sequencing
title: Job Sequencing in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/euphoria/how-to-implement-the-solution.md
- sources/programs/job-sequencing/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
include std/math.e
include std/utils.e
include std/sort.e

-- Indices for value() return value
enum VALUE_ERROR_CODE, VALUE_VALUE, VALUE_NUM_CHARS_READ

-- Indices for parse_int() return value
enum PARSE_INT_VALID, PARSE_INT_VALUE

function parse_int(sequence s)
    -- Trim off whitespace and parse string
    s = trim(s)
    sequence result = stdget:value(s,, GET_LONG_ANSWER)

    -- Error if any errors, value is not an integer, or any leftover characters
    boolean valid = (
        result[VALUE_ERROR_CODE] = GET_SUCCESS
        and integer(result[VALUE_VALUE])
        and result[VALUE_NUM_CHARS_READ] = length(s)
    )

    -- Get value if invalid
    integer value = 0
    if valid
    then
        value = result[VALUE_VALUE]
    end if

    return {valid, value}
end function

-- Indices for parse_int_list() return value
enum PARSE_INT_LIST_VALID, PARSE_INT_LIST_VALUES

function parse_int_list(sequence s)
    -- Split string on comma
    sequence list = split(s, ",")

    -- Parse each item
    integer valid = FALSE
    sequence values = {}
    for n = 1 to length(list)
    do
        sequence result = parse_int(list[n])
        valid = result[PARSE_INT_VALID]
        values &= result[PARSE_INT_VALUE]
        if not valid
        then
            exit
        end if
    end for

    return {valid, values}
end function

procedure usage()
    puts(STDOUT, "Usage: please provide a list of profits and a list of deadlines\n")
    abort(0)
end procedure

-- Indicates for jobs
enum JOB_ID, JOB_PROFIT, JOB_DEADLINE

-- Job sequencing with deadlines
-- Source: https://www.techiedelight.com/job-sequencing-problem-deadlines/
function job_sequencing(sequence profits, sequence deadlines)
    sequence jobs = {}
    integer n = length(profits)

    -- Set up job details
    for k = 1 to n
    do
        jobs &= {{k, profits[k], deadlines[k]}}
    end for

    -- Get longest deadline
    integer longest_deadline = max(deadlines)

    -- Initialize job slots
    sequence slots = repeat({0, 0, 0}, longest_deadline)

    -- Sort jobs by profit then deadline
    jobs = custom_sort(routine_id("compare_jobs"), jobs,, REVERSE_ORDER)

    -- For each job, see if there is available slot at or before the deadline.
    -- If so, store this job in that slot
    for i = 1 to n
    do
        for j = jobs[i][JOB_DEADLINE] to 1 by -1
        do
            if slots[j][JOB_ID] < 1
            then
                slots[j] = jobs[i]
                exit
            end if
        end for
    end for

    return slots
end function

function compare_jobs(sequence job1, sequence job2)
    -- Prioritize by profit, then deadline
    return iif(
        job1[JOB_PROFIT] != job2[JOB_PROFIT],
        job1[JOB_PROFIT] - job2[JOB_PROFIT],
        job1[JOB_DEADLINE] - job2[JOB_DEADLINE]
    )
end function

function get_total_profit(sequence jobs)
    return sum(vslice(jobs, JOB_PROFIT))
end function

-- Check 1st and 2nd command-line argument
sequence argv = command_line()
if length(argv) < 5 or length(argv[4]) = 0 or length(argv[5]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int_list(argv[4])
sequence profits = result[PARSE_INT_LIST_VALUES]
if not result[PARSE_INT_LIST_VALID]
then
    usage()
end if

-- Parse 2nd command-line argument
result = parse_int_list(argv[5])
sequence deadlines = result[PARSE_INT_LIST_VALUES]
if not result[PARSE_INT_LIST_VALID] or length(deadlines) != length(profits)
then
    usage()
end if

-- Get job sequence
sequence job_sequence = job_sequencing(profits, deadlines)

-- Get total profit and display
integer total_profit = get_total_profit(job_sequence)
printf(STDOUT, "%d\n", total_profit)

```

{% endraw %}

Job Sequencing in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).