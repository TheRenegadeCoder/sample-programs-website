If we want to try it ourselves, we can copy the code above into an online 
Common Lisp compiler. The one I linked is in CLISP, but it gets the job done.

Alternatively, as mentioned before, we can download a copy of Steel Bank 
Common Lisp as well as a copy of the solution. Assuming SBCL is in the path, 
we can run a lisp file like a script as follows:

```console
sbcl --script hello-world.lsp
```

And, that should produce the "Hello, World!" string on the command line.
