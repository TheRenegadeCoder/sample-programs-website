---
title: Selection Sort in Bash
layout: default
date: 2020-10-05
featured-image: selection-sort-in-every-language.jpg
last-modified: 2020-10-05

---

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash
# By Jan-Hendrik Ewers (iwishiwasaneagle)
# 04/10/2020

function exit_with_err(){
    USAGE='Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"'
    echo $USAGE
    exit 1
}

N_check=$(echo "$@" | awk -F', ' '{ print NF-1 }')
if [ $N_check -lt 1 ]; then
    exit_with_err
fi

# Read args and spit on ','
IFS=', ' read -r -a array <<< "$@"
N=${#array[@]}

# Selection sort logic
for((i=0;i<N-1;i++));do
    min=${array[$i]}
    ind=$i

    for((j=i+1;j<N;j++));do
        if((array[j]<min));then
            min=${array[$j]}
            ind=$j
        fi
    done

    tmp=${array[$i]}
    array[$i]=${array[$ind]}
    array[$ind]=$tmp
done

# Join array with commas
str=$(printf ', %s' "${array[@]}")
str=${str:2}
echo $str
```

{% endraw %}

[Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Jan-Hendrik Ewers

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).