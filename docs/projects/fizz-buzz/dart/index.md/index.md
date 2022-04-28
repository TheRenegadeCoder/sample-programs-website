# Fizz Buzz in Dart

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Dart
void fizzBuzz(int maxNumber){
  for(int i=1;i<=maxNumber;i++){
    String output = "";
    if(i%3 == 0){
      output += "Fizz";
    }
    if(i%5 == 0){
      output += "Buzz";
    }
    if(output == ""){
      output = "$i";
    }
    print(output);
  }
}

void main() {
  fizzBuzz(100);
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.