---

title: File Io in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the File Io in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
//Written with node 10.16.3
//fs.promises API is still experimental in Node at this time, but it should be preferred over callbacks when is fully developed
fs = require('fs'); 

const filepath = './output.txt'; //create tempfile.txt in this directory

const text = `The quick brown fox jumped over the lazy pupper
The quick brown fox jumped over the lazy dog
The quick brown fox jumped over the lazy doggo
The quick brown fox jumped over the lazy floof`;

function writeFile(){
    fs.writeFile(filepath,text, readFile); //passes writing errors to the callback function, readFile
}

function readFile(err){
    if(err) return console.log(err);
    //fs.readFile is called with 'utf8' option, so the output is a string instead of a buffer
    fs.readFile(filepath,'utf8',printString); //passes (err, string) to the callback function, printString
}

function printString(err, data){
    if(err) return console.log(err); 
    console.log(data);
}

writeFile();

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.