```swift
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

### The Function Signature

Here we see a rather long and punctuation-filled function signature. [Swift functions](https://docs.swift.org/swift-book/LanguageGuide/Functions.html) use named parameters, and the type of each parameter must be noted. This is a safety feature, ensuring, for example, that we don't pass in a float when we need an integer. So, in line 1, we see `start: Int` and `end: Int`, meaning that our function takes in two integer values, named `start` and `end`.

### Default Values

You might think that the equal signs next to each parameter look like assignments, and you would be (sort of) correct. When writing a Swift function's signature, the equals sign can be used to define a default value. If later, the user chooses to call the function without passing in any arguments, the compiler will be smart enough to look at the defaults, and run the function using those values. Swift functions don't *need* to have default values, but they can be nice to have. They can [save you some headaches when building apps](https://www.natashatherobot.com/swift-default-parameter-values/).

### The Return Type

The little arrow after the argument names indicates the return type, which in this case is `Void`. `Void` just means our function doesn't return anything. Our function is only printing out words and numbers, so it isn't returning any values.

[In Swift, if you function doesn't return anything, you can leave off the return type completely, or use the empty tuple `()` to indicate `Void`](https://developer.apple.com/documentation/swift/void). However, I think it's best to just be explicit about what you're returning and write it out.

### Ranges

On line 2, we use the keyword `let` to define a new range of numbers:

```swift
let range = start...end
```

In Swift, [values defined with `let` are immutable](https://stackoverflow.com/a/24048417), and we are encouraged to use them liberally. This keeps us from accidentally changing something when we don't want or need to.

[Ranges](https://developer.apple.com/documentation/swift/range) are their own type in Swift, and allow us to go over a series of numbers without setting up a list or [array](https://developer.apple.com/documentation/swift/array). Although we could have explicitly named the type here, the Swift compiler is able to [infer](http://www.aidanf.net/learn-swift/types_and_type_inference) that we want a range because we've given it two integer values, separated by an ellipsis.

We create a [for-loop](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html) to transverse the range on line 4. [Earlier versions of Swift allowed for C-style loops](https://www.natashatherobot.com/swift-alternatives-to-c-style-for-loops/), but they've since been replaced with this less wordy syntax.

### Conditionals

Line 5 presents a [guard statement](https://medium.com/@chris_dus/the-guard-statement-in-swift-fdad41b08798), a kind of conditional that only fires if a condition has *not* been met. Guard statements are frequently used in Swift to handle edge cases that might otherwise cause errors, and to avoid nested conditionals. Here, we use a guard statement to swiftly print any numbers that are not divisible by 3 or 5. Then, we continue on to the next number.

If a number *is* indeed divisible by 3 or 5, we set up the variable `fizzAndOrBuzz`. This value is defined with [the keyword `var`](https://www.hackingwithswift.com/example-code/language/whats-the-difference-between-let-and-var), which allows us to change it over the course of our function.

We use two if-statements to test for Fizziness and/or Buzziness. Both statements use [the remainder operator](https://www.quora.com/What-does-the-percent-symbol-mean-in-Swift-language), `%`, which gives us the remainder from any division between one integer and another. If one number is evenly divisible by another, the remainder is always 0.

 In other languages, `%` is used for the modulo operator. [Modulo is similar to remainder when dealing with positive integers, but it gives different results when the integers are negative](https://rob.conery.io/2018/08/21/mod-and-remainder-are-not-the-same/). In Swift, the absolute values of the integers are used, so `3 % 15` gives the same result as `3 % -15`.

### Wrapping Up

Line 14 [uses `+=`](https://riptutorial.com/swift/example/1416/concatenate-strings) to add "Buzz" on to the end of our variable, so that if our number is evenly divisible by both 3 and 5, we get the word "FizzBuzz", and not just "Fizz" or just "Buzz".

Finally, we print whatever is inside `fizzAndOrBuzz` at the end of our loop.

We exit the loop, we end the function, and we call `fizzBuzz` at the very bottom. Since we've defined some default values, the script knows to go over the numbers 1 through 100 without having to be told to. We could also pass in arguments for the start and end of our range later, if we want.
