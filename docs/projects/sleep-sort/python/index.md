---

---

Welcome to the Sleep Sort in Python page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
import sys
import threading
from time import sleep


def arg_to_list(string):
    return [int(x.strip(" "), 10) for x in string.split(',')]


def sleep_sort(i, output):
    sleep(i)
    output.append(i)


def error_and_exit():
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    sys.exit()


def main():
    if len(sys.argv) == 1 or not sys.argv[1] or len(sys.argv[1].split(",")) == 1:
        error_and_exit()

    array = arg_to_list(sys.argv[1])

    threads = []
    output = []
    for i in array:
        arg_tuple = (i, output)
        thread = threading.Thread(target=sleep_sort, args=arg_tuple)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(output)


main()

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.