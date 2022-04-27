To run this example, you need to follow a few steps:

1. Run `erlc hello_world.erl` in your terminal to compile the program to a BEAM file - this results in the file `hello_world.beam`
2. In the same directory, open the erlang shell by typing `erl`.
3. Type `l(hello_world).` - remember to end with a period! This is to *load* a module into the shell
4. Run the start function from the module by calling `hello_world:start().` - you should see `Hello, World!` printed to the shell.
5. To exit the shell type `q().` _or_ Ctrl-C, a (abort).
