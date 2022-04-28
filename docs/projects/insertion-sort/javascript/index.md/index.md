---

---

Welcome to the Insertion Sort in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Javascript
const insertionSort =  (arr) => {
    for (let i = 1; i < arr.length; i++){
        let key = arr[i];
        let j = i - 1;
        while (j >= 0  && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}

sanitizeArray = (list) => {
    return list.split(',').map(e => {
       _e = parseInt(e.replace(" ",""));
       if (!_e){ throw new Error();}
       return _e;
    });
 }

 const exit = () => {
     const usage = 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"';
     console.log(usage)
     process.exit();
 }

const main = (input) => {
    try {
        arr = sanitizeArray(input);
        arr.length <= 1 ? exit() : console.log(insertionSort(arr));
    } catch(err) {
        exit();
    }
}

main(process.argv[2])

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.