---

title: Selection Sort in Bash
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Selection Sort in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Bash
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.