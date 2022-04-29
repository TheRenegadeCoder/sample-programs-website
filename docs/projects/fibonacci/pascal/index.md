---

title: Fibonacci in Pascal

---

Welcome to the Fibonacci in Pascal page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Pascal
program Fibonacci(input, output, stdErr);
(*Read count of fibonnaci numbers into a string

*)
var
  buf: String;
  count, check, first,second,result, i : integer;

begin
  (*Variable initialisation must be inside begin-end block*)
  first := 0;
  second := 1;
  result := 0;

  begin   
   buf:= paramStr(1);
   Val(buf, count, check);  
   (*If input is valid integer, check will be 0, else will be 1*)
   if (check <> 0)
   then
   begin
    writeln('Usage: please input the count of fibonacci numbers to output');
   end
   else
    for i := 1 to count do
    begin
    
    result := first + second;
    first := second;
    second := result;
    writeln(i, ': ', first);
    end;
   end;
end.

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.