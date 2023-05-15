FizzBuzz is quite a simple program.
In line 1 the `fizzbuzz` function gets declared. It takes a parameter `num` that determines how far the program should count.
The counting logic takes place in a for-loop in line 2. It starts counting at 1, increases the counter `i` by 1 in every iteration and stops once it reaches `num`.

To understand the main logic of this programm you need to know.

## The modulo (remainder) operator %

>> The remainder operator returns the remainder left over when one operand is divided by a second operand. It always takes the sign of the dividend. ([Mozilla][1])

The trick here is to create a _truthy_ value for the if statements. This is why you can see the `i % 3 == 0` etc. conditionals. If a number is divisible by 3 there will be no remainder, in other words the remainder is true and thus i % 3 == 0 (% 5, % 15) is true in these cases.

Hint: The order of the conditionals matters. If you'd check for example in reverse order, you would print all 3 strings, if the number is divisible by 3 _and_ 5!

Hint: Instead of `i % 15 == 0` you could also write `i % 3 && i % 5`.

Last, but not least, it prints the number via the else clause `else console.log(i);` if none of the conditionals were true.

Extra mile: If you want you can move the conditionals into variables and move them up the scope, right after the second line between the for loop and the first if statement.
For example: `const divisibleBy3 = i % 3`. This way you'd remove the use of [magic numbers][2].

Fun Fact: Despite being a simple programming exercise there is a controversal article about the question [Why can't programmers program?](https://blog.codinghorror.com/why-cant-programmers-program/) that even led to an ["enterprise-class"](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition) version of this game.

[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder
[2]: https://en.wikipedia.org/wiki/Magic_number_(programming)
