# Baklava in Ada

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Ada
with Ada.Text_IO; use Ada.Text_IO;

procedure Baklava is
  M : Integer := 11;
begin
   for I in 1 .. 11 loop
      for J in 1 .. (M-1) loop
        Put(" ");
      end loop;
      for K in 1 .. (2*I - 1) loop
        Put("*");
      end loop;
      M := M -1;
      Put_Line("");
   end loop;
   M:=2;
   for I in reverse 1 .. 10 loop
      for J in 1 .. (M-1) loop
        Put(" ");
      end loop;
      for K in 1 .. (2*I - 1) loop
        Put("*");
      end loop;
      M := M + 1;
      Put_Line("");
   end loop;
end Baklava;
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.