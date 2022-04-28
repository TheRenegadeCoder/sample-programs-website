# File Io in Python

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
def write_file():
    try:
        with open("output.txt", "w") as out:
            out.write("Hi! I'm a line of text in this file!\n")
            out.write("Me, too!\n")
    except OSError as e:
        print(f"Cannot open file: {e}")
        return


def read_file():
    try:
        with open("output.txt", "r") as in_file:
            for line in in_file:
                print(line.strip())
    except OSError as e:
        print(f"Cannot open file to read: {e}")
        return


if __name__ == '__main__':
    write_file()
    read_file()

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.