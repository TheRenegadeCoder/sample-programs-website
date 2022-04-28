# Reverse String in Visual Basic

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Visual Basic
Public Module ReverseString
  Public Sub Main(args() As String)
    Dim input = String.Empty
    If args IsNot Nothing Then
      input = String.Join(" ", args)
    End If

    If String.IsNullOrEmpty(input) Then
      System.Console.Write("Please provide some text to reverse: ")
      input = System.Console.ReadLine()
    End If

    System.Console.WriteLine($"Input: {input}")

    Dim reversedString = ReverseString(input)
    System.Console.WriteLine($"Reversed: {reversedString}")
  End Sub

    Public Function ReverseString(ByVal input As String) As String
        Dim chars() As Char = input.ToCharArray()
        Array.Reverse(chars)
        Return New String(chars)
    End Function
End Module

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.