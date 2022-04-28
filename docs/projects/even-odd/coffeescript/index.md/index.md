# Even Odd in Coffeescript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Coffeescript
USAGE = "Usage: please input a number"
main = (arg) ->
  numberParsed = parseInt(arg)
  isNumber = Number.isInteger(numberParsed)
  if isNumber
    if numberParsed % 2 == 0 then "Even" else "Odd"
  else
    USAGE

console.log main(process.argv[2])
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.