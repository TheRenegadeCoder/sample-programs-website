---
title: Fibonacci in Verilog
layout: default
date: 2019-10-06
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-10-06

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Verilog](https://sampleprograms.io/languages/verilog) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```verilog
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

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Verilog](https://sampleprograms.io/languages/verilog) was written by:

- TheSupremePatel

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).