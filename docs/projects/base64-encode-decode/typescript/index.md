---
authors:
- Arihant Jain
date: 2025-10-14
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-10-14
layout: default
tags:
- base64-encode-decode
- typescript
title: Base64 Encode Decode in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/typescript/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function usageAndExit(): never {
    console.log("Usage: please provide a mode and a string to encode/decode");
    process.exit(1);
}

/**
 * Validates if a string is valid base64 format
 * @param str the string to validate
 * @returns true if valid base64, false otherwise
 */
function isValidBase64(str: string): boolean {
    // Check length is multiple of 4
    if (str.length % 4 !== 0) {
        return false;
    }

    // Only A-Z, a-z, 0-9, +, /, = allowed
    if (!/^[A-Za-z0-9+/]*={0,2}$/.test(str)) {
        return false;
    }

    // = only allowed at end, at most two
    const idx = str.indexOf("=");
    if (idx !== -1 && idx < str.length - 2) {
        // e.g. "ab==cd" is invalid
        return false;
    }

    return true;
}

/**
 * Encodes a string to base64
 * @param input the string to encode
 * @returns base64 encoded string
 */
function encodeBase64(input: string): string {
    // Use Buffer in Node.js
    return Buffer.from(input, "ascii").toString("base64");
}

/**
 * Decodes a base64 string
 * @param input the base64 string to decode
 * @returns decoded string
 */
function decodeBase64(input: string): string {
    // Validate first
    if (!isValidBase64(input)) {
        usageAndExit();
    }
    // Buffer will decode the base64 string
    return Buffer.from(input, "base64").toString("ascii");
}

/**
 * Main function to process command line arguments
 */
function main(): void {
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

// Execute main function
main();

```

{% endraw %}

Base64 Encode Decode in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Arihant Jain

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).