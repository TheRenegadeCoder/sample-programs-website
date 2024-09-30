---
authors:
- Jeremy Grifski
- Manan Gill
date: 2019-10-10
featured-image: file-input-output-in-every-language.jpg
last-modified: 2019-10-11
layout: default
tags:
- file-input-output
- javascript
title: File Input Output in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/javascript/how-to-implement-the-solution.md
- sources/programs/file-input-output/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
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

File Input Output in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Jeremy Grifski
- Manan Gill

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).