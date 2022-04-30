---

title: Selection Sort in Php
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Selection Sort in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Php
<?php

$numbers = array_map('intval', explode(',', $argv[1]));
$array_size = count($numbers);
if ($array_size <= 1)
{
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}


function selection_sort($data)
{
for($i=0; $i<count($data)-1; $i++) {
	$min = $i;
	for($j=$i+1; $j<count($data); $j++) {
		if ($data[$j]<$data[$min]) {
			$min = $j;
		}
	}
    $data = swap_positions($data, $i, $min);
}
return $data;
}

function swap_positions($data1, $left, $right) {
	$backup = $data1[$right];
	$data1[$right] = $data1[$left];
	$data1[$left] = $backup;
	return $data1;
}

echo implode(', ',selection_sort($numbers));
?>
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).