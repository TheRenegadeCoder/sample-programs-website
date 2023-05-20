---
title: The Goby Programming Language
layout: default
date: 2020-05-02
last-modified: 2022-05-11
featured-imaged: programming-languages.jpg
tags: [goby]
authors:
  - the_renegade_coder

---

Welcome to the Goby page! Here, you'll find a description of the language as well as a list of sample programs in that language.

## Description

[According to the GitHub project](https://github.com/goby-lang/goby), 
Goby, formerly known as Rooby, is a Ruby-like language written in Go. 
The goal of the language is to provide a small environment for building 
microservices and API servers. 

Beyond that, the project didn't have much to offer in terms of
use cases or samples. That said, the official website does give a few
examples of language features including:

- Concurrency Support
- Builtin Multi-threaded Server
- Plugin System

For anyone who would like to give the language a try, Goby can be installed
and ran in REPL mode with the following commands:

```shell
brew tap goby-lang/goby
brew install goby
goby -i
```

Alternatively, you can try running all the sample code snippets using
the samplerunner script included in the repo:

```shell
./samplerunner.sh run -l goby
```

Feel free to browse some of the articles in the following section to see
the language in action.


## Articles

- [Hello World in Goby](https://sampleprograms.io/projects/hello-world/goby)