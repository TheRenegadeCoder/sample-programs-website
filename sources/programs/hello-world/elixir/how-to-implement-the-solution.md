Alright, let's get right to it.

As we can see, Hello World in Elixir is just a single line of
code. As usual, let's dig into it a bit.

Up first, we have a reference to the IO module. In Elixir, the `IO`
module is the standard tool for working with standard input and 
output as well as files and other devices. So, it makes sense that 
we'd use it here to gain access to standard output.

Up next, we call the `puts` function of the `IO` module. Like print in 
most languages, `puts` simply writes a value to standard output. In 
fact, we aren't limited to standard output. We can redirect the output 
to other streams such as standard error:

```elixir
IO.puts :stderr, "Uh Oh!"
```

At any rate, `puts`, in our primary example, will simply write "Hello, 
World!" to the user. To be honest, I'm surprised this is only the 
second time we've seen the `puts` keyword in this series, the first being 
Ruby.
