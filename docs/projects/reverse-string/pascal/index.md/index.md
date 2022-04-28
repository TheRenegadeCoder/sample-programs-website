# Reverse String in Pascal

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Pascal
program reversestring(input, output, stdErr);
(*Accept a String from Command Line, Reverse it & Print it*)
var
  i, j: Integer;
   buf, result: String;
begin
buf := paramStr(1);
  if buf = '' then
    writeln('Usage: please provide a string')
  else;
  setlength(result,length(buf));
  i:=1; 
  j:=length(buf);
  while (i<=j) do
    begin
      result[i]:=buf[j-i+1];
      inc(i);
    end;
    writeln(result);
end.

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.