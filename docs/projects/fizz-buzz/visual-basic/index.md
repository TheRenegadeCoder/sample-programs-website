---

---

Welcome to the Fizz Buzz in Visual Basic page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Visual Basic
Option Explicit On
Module FizzBuzz
    Public Sub Main()
        FizzBuzz()
    End Sub
    Sub FizzBuzz()
        Dim first = True
        Dim i As Integer
        For i = 1 To 100
            If i Mod 15 = 0 Then
                If first Then
                    System.Console.Write("FizzBuzz")
                    first = False
                Else
                    System.Console.Write(", FizzBuzz")
                End If

            ElseIf i Mod 5 = 0 Then
                If first Then
                    System.Console.Write("Buzz")
                    first = False
                Else
                    System.Console.Write(", Buzz")
                End If
            ElseIf i Mod 3 = 0 Then
                If first Then
                    System.Console.Write("Fizz")
                    first = False
                Else
                    System.Console.Write(", Fizz")
                End If
            Else
                If first Then
                    System.Console.Write(Str(i))
                    first = False
                Else
                    System.Console.Write($", {Str(i)}")
                End If
            End If
        Next
    End Sub
End Module

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.