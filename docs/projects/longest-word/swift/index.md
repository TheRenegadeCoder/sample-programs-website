---
authors:
- ShawnN003
date: 2025-02-18
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-02-18
layout: default
tags:
- longest-word
- swift
title: Longest Word in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/swift/how-to-implement-the-solution.md
- sources/programs/longest-word/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

if (CommandLine.arguments.count < 2) {
    print("Usage: please provide a string")
}
else 
{
    var sentence = CommandLine.arguments[1]   
    sentence = sentence.replacingOccurrences(of: "\n", with: "")    //removing the break line if it contains any
    longestWord(input : sentence)
}

func longestWord(input : String) -> Void
{
    var longest = 0
    var testWord = ""

    if(input == "")
    {
         print("Usage: please provide a string")    //checking for empty string
    }

    else 
    {
        var substrings: [Substring] = []    //array to hold the array of the input strings
        substrings = input.split(separator: " ")        //splitting the array by spaces
        
        for word in substrings    //iterate through the array
        {
            testWord = word.trimmingCharacters(in: CharacterSet(charactersIn: " "))
            if(testWord.count > longest)    
            {
                longest = testWord.count    //obtaining the longest count of words
            }
        }
        print(longest)
    }
}

```

{% endraw %}

Longest Word in [Swift](https://sampleprograms.io/languages/swift) was written by:

- ShawnN003

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).