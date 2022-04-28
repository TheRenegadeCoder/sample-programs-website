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
