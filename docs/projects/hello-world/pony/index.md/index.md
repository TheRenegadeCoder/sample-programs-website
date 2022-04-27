# Hello World in Pony

## Solution

```Pony
actor Main
  new create(env: Env) =>
    env.out.print("Hello, World!")

```