# Fizz Buzz in Vimscript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Vimscript
func! FizzBuzz()
    for l:i in range(1, 100)
        if l:i % 15 == 0
            let l:str = 'FizzBuzz'
        elseif l:i % 5 == 0
            let l:str = 'Buzz'
        elseif l:i % 3 == 0
            let l:str = 'Fizz'
        else
            let l:str = l:i
        endif

        call append(l:i-1, l:str)
    endfor

    " go to top of buffer
    normal gg
endfunc

au BufEnter,BufReadPost * call FizzBuzz()

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.