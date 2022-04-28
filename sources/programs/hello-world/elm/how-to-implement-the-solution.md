As usual, let's dive right into the implementation of 
Hello World in Elm:

```elm
module HelloWorld exposing (..)
import Html exposing (text)
main =
  text "Hello, World!"
```

And, that's it! We can write Hello World in Elm in just 
a few lines of code, but what's really going on in this 
code?

Up first, we have the module declaration line. In other 
words, we've defined a module with the name HelloWorld. 
If anyone wanted to use this module, everything would be 
completely exposed.

In the third line, we import the Html module, so we can 
access the text functionality. As we can probably imagine, 
the text function just displays text to the user.

Finally, as with many functional languages, we have the 
main function. To no surprise, the main function is a 
special function which provides the starting point for 
the program. In the case of Elm, the main function must 
retain an element to draw into the page. In our case, we're 
returning a HTML element from the text function.
