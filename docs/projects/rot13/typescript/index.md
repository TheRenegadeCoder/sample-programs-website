---
authors:
- Ferrel John Fernando
date: 2024-10-09
featured-image: rot13-in-every-language.jpg
last-modified: 2024-10-09
layout: default
tags:
- rot13
- typescript
title: Rot13 in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/typescript/how-to-implement-the-solution.md
- sources/programs/rot13/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function rot13(input: string): string {
  if (!input) {
      return "Usage: please provide a string to encrypt";
  }

  return input.split('').map(char => {
      const code = char.charCodeAt(0);
      // Check if the character is an uppercase letter
      if (code >= 65 && code <= 90) {
          return String.fromCharCode((code - 65 + 13) % 26 + 65);
      }
      // Check if the character is a lowercase letter
      else if (code >= 97 && code <= 122) {
          return String.fromCharCode((code - 97 + 13) % 26 + 97);
      }
      // If it's not a letter, return the character unchanged
      return char;
  }).join('');
}

const args = process.argv.slice(2);

if (args.length !== 1) {
  console.log("Usage: please provide a string to encrypt");
  process.exit(1);
} else {
  const input = args[0];
  const result = rot13(input);
  console.log(result);
}

```

{% endraw %}

Rot13 in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Ferrel John Fernando

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).