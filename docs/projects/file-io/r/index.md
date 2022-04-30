---

title: File Io in R
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the File Io in R page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```R
file_create_result = tryCatch({
#Open and write 2 lines to the file.
  fileConn<-file("output.txt")
  writeLines(c("Hello","World\n"), fileConn)
  writeLines(c("Writing this file using R"), fileConn)
  close(fileConn)
},
 warning = function( w )
  {
     cat("Warning while opening the file")
  },
   error = function( w )
  {
     cat("Error while opening the file")
  }
)
# Catch File Open Error
if(file.exists("output.txt")){
  f_open = readLines("output.txt")
  singleString <- paste(readLines("output.txt"), collapse=" ")
  cat(singleString)
} else{
  cat("File doesn't exist")
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).