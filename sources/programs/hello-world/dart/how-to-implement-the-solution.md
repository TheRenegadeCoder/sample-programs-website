Coming from a Java background, the following snippet of code is downright
stripped to the barebones.

```dart
void main() => print('Hello, World!');
```

In order to implement Hello World in Dart, developers need to understand only
three concepts like main methods, strings, and arrow functions. But look at the
code above, it seems deceptively easy, right?

What is going on is “main()” only does one thing, print the phrase “Hello, World!”.
We’ll dig into how and why all of this happens in a bit. But it’s important to
step away for a bit and just look at what’s there and acknowledge how simple it is.

In a Dart project, only one class would have a main method (“main()”). A main
method is how every Dart program knows where to start. Therefore, every program
must have exactly one of these main methods implemented. Don’t worry too much
about the syntax. Just know that we need a main method.

Then we have to output our greeting (“Hello, World!”) to the command line. To
do so, we have to leverage a static method out of Dart’s built-in library. It’s
the “print” statement. It’s a method like “main()” only difference is we put a
string inside the parentheses. It tells the computer to take the string and
print out so we can read it.

The last concept are arrow functions (“=>”). These are methods like print or,
in this case, main that only do one thing. Because they only do one thing, we
can use “=>” from the method’s definition (“main()”) directly to the logic.
Other more complex methods may require the use of “return”. But that’s not
required in this case.
