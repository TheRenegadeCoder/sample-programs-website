---
authors:
- alope107
date: 2026-05-18
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-05-18
layout: default
tags:
- file-input-output
- ocaml
title: File Input Output in OCaml
title1: File Input
title2: Output in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/ocaml/how-to-implement-the-solution.md
- sources/programs/file-input-output/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](/projects/file-input-output) in [OCaml](/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let filename = "output.txt"

let sample_text =
  {|Some mundane sample text
Some sample text that is mundane
Another line of mundane sample text
|}

let () =
  (try
     Out_channel.with_open_text filename (fun oc ->
         Out_channel.output_string oc sample_text)
   with Sys_error msg ->
     Printf.eprintf "Failed to write to '%s': %s\n" filename msg;
     exit 1);

  (try In_channel.with_open_text filename (fun ic -> In_channel.input_lines ic)
   with Sys_error msg ->
     Printf.eprintf "Failed to read from '%s': %s\n" filename msg;
     exit 1)
  |> List.iter print_endline

```

{% endraw %}

File Input Output in [OCaml](/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).