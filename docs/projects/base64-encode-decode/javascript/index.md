---
authors:
- Eshaan Walia
date: 2025-10-06
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-10-06
layout: default
tags:
- base64-encode-decode
- javascript
title: Base64 Encode Decode in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/javascript/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
#!/usr/bin/env node

function usageAndExit() {
  console.error("Usage: please provide a mode and a string to encode/decode");
  process.exit(1);
}

function isValidBase64(str) {
  // Check length multiple of 4
  if (str.length % 4 !== 0) return false;
  // Only A–Z, a–z, 0–9, +, /, = allowed
  if (!/^[A-Za-z0-9+/]*={0,2}$/.test(str)) return false;
  // = only allowed at end, at most two
  const idx = str.indexOf("=");
  if (idx !== -1 && idx < str.length - 2) {
    // e.g. “ab==cd” invalid
    return false;
  }
  return true;
}

function encodeBase64(input) {
  // Use Buffer in Node.js
  return Buffer.from(input, "ascii").toString("base64");
}

function decodeBase64(input) {
  // Validate first
  if (!isValidBase64(input)) {
    usageAndExit();
  }
  // Buffer will ignore invalid trailing bits
  return Buffer.from(input, "base64").toString("ascii");
}

function main() {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    usageAndExit();
  }
  const mode = args[0];
  const text = args[1];

  if (!text) {
    usageAndExit();
  }

  if (mode === "encode") {
    console.log(encodeBase64(text));
  } else if (mode === "decode") {
    console.log(decodeBase64(text));
  } else {
    usageAndExit();
  }
}

if (require.main === module) {
  main();
}


```

{% endraw %}

Base64 Encode Decode in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Eshaan Walia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).