---

title: Capitalize in R
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Capitalize in R page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```R
args<-commandArgs(TRUE)
if(length(args) > 0){
  if (args[1] != ""){
    len = length(args)
    array_string <- strsplit(args[1], "")[[1]]
    for (i in 1:len){
        if (i == 1){
          array_string[i] <- toupper(substr(array_string[i], 1, 1))
        }
        #Convert to Character Vector.... else prints with spaces in between 
        a = as.character(array_string)
        cat(a,fill = FALSE, sep = "")
    }
  }else{
    cat("Usage: please provide a string")
  }
}else{
    cat("Usage: please provide a string")
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.