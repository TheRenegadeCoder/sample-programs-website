# Fizz Buzz in Swift

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Swift
func fizzBuzz(start: Int = 1, end: Int = 100) -> Void {
    let range = start...end
    
    for number in range {
        guard number % 5 == 0 || number % 3 == 0 else {
            print(number)
            continue
        }
        
        var fizzAndOrBuzz = ""
        
        if number % 3 == 0 {
            fizzAndOrBuzz = "Fizz"
        }
        
        if number % 5 == 0 {
            fizzAndOrBuzz += "Buzz"
        }
        
        print(fizzAndOrBuzz)
    }
}

fizzBuzz();
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.