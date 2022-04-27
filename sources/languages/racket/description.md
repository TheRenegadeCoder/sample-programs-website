Well, at this point, Wikipedia has yet to fail me. As usual, I referenced 
it to learn a little bit more about today’s language.

Like Python and Java, Racket is a general-purpose programming language. 
Unfortunately, that’s sort of where the similarities stop. After all, 
Racket comes from the Lisp-Scheme family, so it resembles a typical 
functional programming language. In other words, expect plenty of parentheses.

What makes Racket different from its Lisp counterparts is its extensibility. 
In other words, the language can be easily modified using macros. Remember 
when we learned about macros in Rust? Same idea. We can use these macros to 
control the syntax of Racket.

Macros alone aren’t interesting enough to warrant any excitement. However, 
mix macros with a module system, and we get an extremely versatile language. 
These modules allow us to import various macros that can be used to control 
the dialect of Racket. For instance, if we wanted a statically typed version 
of Racket, there’s a module for that: typed/racket.
