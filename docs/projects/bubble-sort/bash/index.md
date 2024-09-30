---
authors:
- Lucas Schaan
date: 2019-10-01
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-01
layout: default
tags:
- bash
- bubble-sort
title: Bubble Sort in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/bash/how-to-implement-the-solution.md
- sources/programs/bubble-sort/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Bubble Sort in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Lucas Schaan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).