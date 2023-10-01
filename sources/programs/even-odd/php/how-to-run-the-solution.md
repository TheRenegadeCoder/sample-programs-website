
 ```php
 
<?php
// Define a function to check if a number is even or odd
function checkEvenOdd($number) {
    if ($number % 2 == 0) {
        echo "$number is even.";
    } else {
        echo "$number is odd.";
    }
}

// Test the function with a number
$number = 7; // You can change this number to test different values

// Call the function to check if the number is even or odd
checkEvenOdd($number);
?>


```

```console
php name.php
```