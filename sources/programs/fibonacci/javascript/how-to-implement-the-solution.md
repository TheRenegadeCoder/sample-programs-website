Let's look at the code in detail:  

Here we have a function called `fibonacci` that takes in a numeric value as an argument that corresponds to the amount Fibonacci numbers we want to print in succession.

What `fibonacci`" does is that it starts printing from 1 then each time it just prints the accumulation of the last number it printed (stored in variable named `second`) and the 2nd last number it printed (stored in variable named `first`).

Then we have a variable named `num` which can have a numeric value of `10` since we want to print the first 10 numbers in the Fibonacci sequence. I can also have the value `process.argv[2]` so we can run the command `node fibonacci.js 10` to execute the file with NodeJS and print the first 10 numbers in the Fibonacci sequence.

Then we have a function that verifies that `num` has a positive, numeric value so we can run the function named `fibonacci`, else it just returns an instruction/warning.
