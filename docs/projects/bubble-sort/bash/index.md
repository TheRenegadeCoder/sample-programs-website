---
title: Bubble Sort in Bash
layout: default
date: 2019-10-01
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-01

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

ERROR="Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""

function bubble-sort {
    new_array=(${array[@]::${#array[@]}-1}) #all elements except the last one
    for i in "${!array[@]}"; do
        switch=false;
        for j in "${!new_array[@]}" ; do
            if [ "${array[j]}" -gt "${array[j+1]}" ]; then
                aux=${array[j]}
                array[j]=${array[j+1]}
                array[j+1]=$aux
                switch=true;
            fi;
        done;
        if [ $switch = false ]; then 
            break; 
        fi;
    done;
}

#Validation to fit criteria
if [ "$#" != "1" ]; then echo $ERROR; exit 1; fi; #wrong input
if [[ ! "$1" =~ "," ]]; then echo $ERROR; exit 1; fi; #wrong format

array=($(echo $@ | tr ", " " "))

if [ "${array[0]}" == "" ]; then echo $ERROR; exit 1; fi; #empty input
if [ "${#array[@]}" == "1" ]; then echo $ERROR; exit 1; fi; #not a list

bubble-sort array
arrayString=${array[@]}
echo "${arrayString//" "/", "}"
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Lucas Schaan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 01 2019 22:46:49. The solution was first committed on Oct 01 2019 16:34:54. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).