---

title: Import/Export in Every Language
layout: default
date: 2019-10-04
last-modified: 2020-11-01
featured-image:
tags: [import-export]
authors: 
  - ray6464
  - the_renegade_coder

---

Welcome to the Import Export page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

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

- [Import Export in C](https://sampleprograms.io/projects/import-export/c)
- [Import Export in C++](https://sampleprograms.io/projects/import-export/c-plus-plus)
- [Import Export in Javascript](https://sampleprograms.io/projects/import-export/javascript)
- [Import Export in Typescript](https://sampleprograms.io/projects/import-export/typescript)