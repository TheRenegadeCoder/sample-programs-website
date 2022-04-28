# Fibonacci in Verilog

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Verilog
//Verilog code Listing first 25 Fibonacci numbers till

module Fibonacci();

integer previous_value = 0;
integer current_value = 1;
integer clk = 0;

always #1 
    clk = ~clk;

always @(posedge clk)
begin
    current_value <= current_value + previous_value;
    previous_value <= current_value;
    $display("%0d", current_value);
end

initial #50 //Prints 25 fibonacci numbers as values change at POSEDGE of clock
    $finish;

endmodule


```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.