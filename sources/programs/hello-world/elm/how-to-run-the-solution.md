Okay, so we have a solution, but how do we run it? Well, 
Elm is a bit different than our typical languages because 
it's for web use only. As a result, we'll want to download 
the necessary utilities first.

Now would be a good time to install Elm. With that installed, 
get the Html package from the command line:

```shell
elm-package install elm-lang/html
```

After that, grab a copy of the elm solution from GitHub. Now, 
in the same folder as the new file, run the following from the 
command line:

```shell
elm reactor
```

This will basically launch a local server for testing. Now, go 
to the local server location in a browser and open the HelloWorld 
file. That's it!

Alternatively, use an online Elm compiler for testing code snippets. 
Give it a go!
