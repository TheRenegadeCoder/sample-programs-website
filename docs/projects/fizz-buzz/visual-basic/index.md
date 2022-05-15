---

title: Fizz Buzz in Visual Basic
layout: default
date: 2022-04-28
last-modified: 2022-05-15

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual basic
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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Thomas Braccia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 01 2020 19:15:54. The solution was first committed on Oct 01 2020 18:54:14. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).