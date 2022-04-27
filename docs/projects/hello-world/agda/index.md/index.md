# Hello World in Agda

## Solution

```Agda
module helloworld where
  open import IO
  main = run (putStrLn "Hello, World!")

```