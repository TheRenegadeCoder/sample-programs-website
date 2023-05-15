Let's start by looking at the complete algorithm to reverse a string in Visual Basic.

As we can see, VB.NET is a structured language. In other words, there's a very 
strong focus on code blocks and control flow structures.

Our first code block is the module declaration. In this case, we've declared a
public module called `ReverseString`. If other libraries needed access to this module,
they could simply import it by name.

### The `Main()` Function

Next, we have our typical main function declaration. Of course, in VB.NET, we
call them subroutines rather than functions, as indicated by the `Sub` keyword.

The first thing we do in our `Main` function is create a variable named `input` to store the value to be reversed.

```vb
Public Sub Main(args() As String)
    Dim input = String.Empty
```

We then need to populate the `input` variable from the value entered at the command prompt. We can use an array of command line arguments using `args()` as the paramater in `Main()`
As input with spaces will be treated as multiple arguments in the `args()` array we need to build them into the single string `input`.

```vb
If args IsNot Nothing Then
    input = String.Join(" ", args)
End If
```

We first check that there are arguments to join, and if there are join them with the `String.Join()` function, which takes an array of `args` and joins them together with a space `" "` between them, thereby recreating what was entered at the command line.


Finally, we output to the console with the `System.Console.Writeline` function. 

```vb
System.Console.WriteLine(ReverseString(input))
```

Here we call the `ReverseString()` function with `input` as our argument. We will see below how `ReverseString()` operates and returns to us the reversed string. The reversed string is then passed into the `WriteLine` function and it is output to the console.

### The `ReverseString()` function

Let's take a look at how this function reverses a string.

```vb
Public Function ReverseString(ByVal input As String) As String
    Dim chars() As Char = input.ToCharArray()
    Array.Reverse(chars)
    Return New String(chars)
End Function
```

We take in the value to be reversed into a local variable named `input`.
In order to reverse it we need to convert the string variable `input` into a character array named `chars()`.

```vb
'i.e.: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'] 
Dim chars() As Char = input.ToCharArray()
```

The character array `chars` can be reversed using the the `Array.Reverse()` function

```vb
'i.e.: ['!', 'd', 'l', 'r', 'o', ',W, ' ', ',', 'o', 'l', 'l', 'e', 'H']
Array.Reverse(chars)
```

Finally, the character array `chars` is converted/combined into a string and returned.

```vb
Return New String(chars)
```

This function executes correctly with any ASCII string. I also executes with an empty string as input.
