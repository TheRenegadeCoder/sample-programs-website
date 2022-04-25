# Import Export in Every Language

## Description

Exporting and importing data is required to create modules. For this project, we want to create 
variables in one file (say this file's name is "export") and export them from the "export" file. 
Then, import them from another file (say the file's name is "import"), and use them in the 
"import" file.


## Requirements

To satisfy these requirements, both files must be in the same folder. Then, the `export` file must 
contain a variable with some value. If everything works correctly, we should be able to execute 
`import` as follows:

```shell
$ ./import.lang
$ "Sample Programs"
```

In this case, the import script loaded a variable containing the value "Sample Programs" and
printed it to the user. For consistency and testing purposes, we ask that all `export` files
store this value.


## Testing

The following table contains various test cases that you can use to verify the correctness of 
your solution: 

| Description       | Output            |
|-------------------|-------------------|
| Standard Behavior | "Sample Programs" | 

As always, these tests will be run against any code submitted to the repo via [Glotter][glotter-github].


## Articles

