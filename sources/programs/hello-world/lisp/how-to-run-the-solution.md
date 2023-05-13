If we want to try it ourselves, we can copy the code above into an
[online Common Lisp compiler][1]. The one I linked is in CLISP, but it gets the job done.

Alternatively, as mentioned before, we can download a copy of
[Steel Bank Common Lisp][2] as well as a [copy of the solution][3].
Assuming SBCL is in the path, we can run a lisp file like a script as follows:

```console
sbcl --script hello-world.lsp
```

And, that should produce the "Hello, World!" string on the command line.

[1]: https://ideone.com/l/common-lisp-clisp
[2]: https://www.sbcl.org/platform-table.html
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/l/lisp/hello-world.lsp
