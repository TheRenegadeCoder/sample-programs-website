---

---

Welcome to the Fizz Buzz in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Php
<?php

for ($i = 1; $i < 101; $i++)
{
  $output = "";

  if ($i % 3 == 0)
  {
    $output .= "Fizz";
  }

  if ($i % 5 == 0)
  {
    $output .= "Buzz";
  }

  if (!$output)
  {
    $output = $i;
  }

  echo $output . "\n";
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.