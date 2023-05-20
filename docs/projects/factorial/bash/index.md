---
title: Factorial in Bash
layout: default
date: 2019-10-09
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-09

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

number=$1

if [[ -z "$number" ]]
then
    echo "Usage: please input a non-negative integer"
    exit 1
fi

if ! [[ "$number" =~ ^[0-9]+$ ]]  
then 
        echo "Usage: please input a non-negative integer"
        exit 1
fi

value=1

while [ $number -gt 1 ]
do

  value=$((value * number))
 
  number=$((number - 1))

done

echo $value
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Amanda Hager Lopes de Andrade Katz

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).