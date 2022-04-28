---

---

# Insertion Sort in Php

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Php
<?php

function insertion_Sort($my_array)
{
	for($i=0;$i<count($my_array);$i++){
		$val = $my_array[$i];
		$j = $i-1;
		while($j>=0 && $my_array[$j] > $val){
			$my_array[$j+1] = $my_array[$j];
			$j--;
		}
		$my_array[$j+1] = $val;
	}
    return $my_array;
}

$test_array = array_map('intval', explode(',', $argv[1]));
$array_size = count($test_array);

if ($array_size <= 1)
{
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

$out = insertion_Sort($test_array);
echo implode(', ', $out);
?>

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.