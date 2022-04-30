---

title: Bubble Sort in Php
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Bubble Sort in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

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


for ( $i = 0; $i < $array_size; $i++ )
{
   for ($j = 0; $j < $array_size; $j++ )
   {
      if ($numbers[$i] < $numbers[$j])
      {
         $temp = $numbers[$i];
         $numbers[$i] = $numbers[$j];
         $numbers[$j] = $temp;
      }
   }
}

echo implode(', ', $numbers);

?>
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).