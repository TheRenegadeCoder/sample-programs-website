---

title: Capitalize in Pascal

---

Welcome to the Capitalize in Pascal page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Pascal
program Capitalise(input, output, stdErr);
(* Accept a String from commandline, convert first character to upper case
   Pascal Strings begins with 1, not 0
*)
var
buf: string;
begin
  buf := paramStr(1);
  if buf = ''  then
    writeln('Usage: please provide a string')
  else
    buf[1] := UpCase(buf[1]);
    writeln(buf);
end.

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.