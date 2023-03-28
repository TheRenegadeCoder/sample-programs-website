---

title: Bubble Sort in Visual Basic
layout: default
date: 2022-04-28
last-modified: 2023-03-28

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual basic
Public Module BubbleSort
    Public Sub Main(args As String())
        Console.WriteLine("GetCommandLineArgs: {0}", String.Join(", ", args))
        Dim listOfStringInputs = args.ToList
        Dim sortArray = listOfStringInputs.ConvertAll(Function(inputs) Int32.Parse(inputs)).ToArray

        sortArray = BubbleSort(sortArray)
        Dim outputSorted As String = String.Join(", ", sortArray)
        System.Console.WriteLine($"Sorted: {outputSorted}")
    End Sub

    Public Function BubbleSort(sortArray As Integer())
        Dim holdInt
        For i = 0 To UBound(sortArray)
            For x = UBound(sortArray) To i + 1 Step -1
                If sortArray(x) < sortArray(i) Then
                    holdInt = sortArray(x)
                    sortArray(x) = sortArray(i)
                    sortArray(i) = holdInt
                End If
            Next x
        Next i
        Return sortArray
    End Function
End Module
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Thomas Braccia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 01 2020 19:12:59. The solution was first committed on Oct 01 2020 15:35:27. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).