# Fizz Buzz in Java

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Java
public class FizzBuzz {
  public static void main(String[] args) {
    for (int i = 1; i < 101; i++) {
      String output = "";
      if (i % 3 == 0) {
        output += "Fizz";
      }
      if (i % 5 == 0) {
        output += "Buzz";
      }
      if (output.isEmpty()) {
        output += i;
      }
      System.out.println(output);
    }
  }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.