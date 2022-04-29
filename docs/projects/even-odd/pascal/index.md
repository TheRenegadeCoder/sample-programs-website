---

---

Welcome to the Even Odd in Pascal page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Pascal
program a1(input, output, stdErr);
(* Read Number from commandline, print  Even or Odd *)
var
 buf: String;
 a, check:integer;
begin    
  buf:= paramStr(1);
    Val(buf, a, check) ;
    if check <> 0
    then
    writeln('Usage: please input a number')
    else
    begin
        if( (a mod 2) = 0) then
            begin
            writeln('Even'); 
            end         
        else
            begin
            writeln('Odd'); 
            end
    end
end.

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.