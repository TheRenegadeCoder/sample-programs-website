Let's go ahead and dig into our implementation of Hello World in Racket.

Up first, we have this peculiar line that looks kind of like a comment in Python
or an import in C. As it turns out, the `lang` line specifies the language used by
the interpreter. In fact, I already mentioned that there's a module which
provides syntax for static typing in Racket.

In this case, the language we have chosen is `racket/base`. This only provides us
the core Racket functionality. As an alternative, we could have easily specified
racket alone.

Finally, we have our print line. To be honest, we could have used the print
functionality:

```racket
#lang racket/base
(print "Hello, World!)
```

However, I wanted to show that you can implement Hello World without the mess of
parentheses. That's because Racket automatically prints constants. If we had a
slightly more complicated expression:

```racket
#lang racket
+ 2 2
```

We would see the three constants returned to us in their stack order:

```racket
#<procedure:+>
2
2
```

We would need parentheses to actually evaluate this expression.
