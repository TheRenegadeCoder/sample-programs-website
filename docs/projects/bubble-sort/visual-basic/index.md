---

title: Bubble Sort in Visual Basic
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Bubble Sort in Visual Basic page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Visual Basic
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).