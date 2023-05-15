Let's look at the code in detail.

### Main Function

```python
if __name__ == "__main__":
    nums = error_handling(sys.argv)
    print(maximum_subarray(nums))
```

This bit of code checks to see if this is the `main` module run. If true, then it calls the `error_handling`
function to convert the command-line arguments to a list of integers. It calls the `maximum_subarray`
function to calculate the maximum subarray value. Finally, it calls the `print` function to display
the value.

### Error Handling Function

```python
def error_handling(argv: List) -> List[int]:
    str_input = (','.join(i for i in argv[1:])).strip()
    if str_input == "":
        print('Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"')
        sys.exit(1)
    nums = [int(num) for num in str_input.split(',')]
    return nums
```

This bit of code takes a comma-separated string of integers from the command-line (via the `sys.argv`). It then converts the string into an array of integer. It also deals with the edge case which arises when there is no input or the input string is empty (blank string).
If it is empty, the usage is displayed, and the program exits. Otherwise, the command-separated string is converted to a list of integers.

### Maximum Subarray

```python
def maximum_subarray(nums: List[int]) -> int:
    local_max = 0
    global_max = nums[0]
    for num in nums:
        local_max += num
        if (local_max < 0):
            local_max = 0
        elif global_max < local_max:
            global_max = local_max
    return global_max
```

This function implements Kadane's algorithm. It first initializes `global_max`
(the final value to be returned from the function) to the first element of the array (`nums`)
and `local_max` as 0. It then iterates through the array, keeps adding values to `local_max`.
If `local_max` goes to less than 0, then `local_max` is set to 0. Otherwise, if `local_max`
is greater than `global_max`, `global_max` is set to the value of `local_max`.

Once all the values are processed, `global_max` is returned.

For example, if `-1, -2, 1, 2, 3` is the input:

- Initialize `local_max` to `-1` (the first value) and `global_max` to `0`.
- Now, iterator through all of the values.
- For the first two values, the value of `local_max` is `0`: `0 + (-1) < 0` and `0 + (-2) < 0`, so `-1` and `-2` are skipped.
- For the remaining values, `local_max` is accumulated and `global_max` is updated with `local_max`:
  - `local_max` is `0 + 1 = 1`, and `1 < 0` is false, so `local_max` is not reset, and `-1 < 1`, so `global_max` is set to `1`
  - `local_max` is `1 + 2 = 3`, and `3 < 0` is false, so `local_max` is not reset, and `1 < 3`, so `global_max` is set to `3`
  - `local_max` is `3 + 3 = 6`, and `6 < 0` is false, so `local_max` is not reset, and `3 < 6`, so `global_max` is set to `6`
- Finally, `global_max` (`6`) is returned
