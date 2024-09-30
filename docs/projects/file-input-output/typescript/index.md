---
authors:
- Antonino Bertulla
date: 2023-10-04
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-10-04
layout: default
tags:
- file-input-output
- typescript
title: File Input Output in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/typescript/how-to-implement-the-solution.md
- sources/programs/file-input-output/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
import { Readable } from "stream";
import * as fs from 'fs'

const filepath = './output.txt'; //create tempfile.txt in this directory
const write$ = fs.createWriteStream(filepath);
write$.on('finish', () => fs.createReadStream(filepath).on('error', console.error).pipe(process.stdout));
write$.on('error', console.error);

const readableStream = new Readable();
const texts = [
  'The quick brown fox jumped over the lazy pupper\n',
  'The quick brown fox jumped over the lazy dog\n',
  'The quick brown fox jumped over the lazy doggo\n',
  'The quick brown fox jumped over the lazy floof'
];

for (const text of texts) {
    readableStream.push(text);
}
readableStream.push(null);

readableStream.pipe(write$)

```

{% endraw %}

File Input Output in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Antonino Bertulla

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).