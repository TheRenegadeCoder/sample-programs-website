# File Io in R

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.