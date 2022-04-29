---

title: Bubble Sort in Bash

---

Welcome to the Bubble Sort in Bash page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Bash
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.