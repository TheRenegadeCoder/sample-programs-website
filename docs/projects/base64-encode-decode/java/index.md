---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-04-10
layout: default
tags:
- base64-encode-decode
- java
title: Base64 Encode Decode in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/java/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class Base64EncodeDecode {
    public static void main(String[] args) {
        if (args == null || args.length != 2) {
            usage();
        }

        String mode = args[0];
        String input = args[1];

        if (mode == null || input == null || mode.isEmpty() || input.isEmpty()) {
            usage();
        }

        switch (mode) {
            case "encode" -> encode(input);
            case "decode" -> decode(input);
            default -> usage();
        }
    }

    private static void encode(String input) {
        byte[] bytes = input.getBytes(StandardCharsets.UTF_8);
        String encoded = Base64.getEncoder().encodeToString(bytes);
        System.out.println(encoded);
    }


    private static void decode(String input) {
        if (!looksLikeBase64(input)) {
            usage();
        }

        try {
            byte[] decoded = Base64.getDecoder().decode(input);
            String output = new String(decoded, StandardCharsets.UTF_8);
            System.out.println(output);
        } catch (IllegalArgumentException ex) {
            usage();
        }
    }

    private static boolean looksLikeBase64(String input) {

        if (input.isEmpty() || (input.length() % 4 != 0)) {
            return false;
        }

        int len = input.length();
        int pad = 0;

        for (int i = 0; i < len; i++) {
            char c = input.charAt(i);

            if (c == '=') {
                pad++;
            } else {
                if (pad > 0) return false; // padding only at end
                if (!isBase64Char(c)) return false;
            }
        }

        int padCount = 0;
        for (int i = input.length() - 1; i >= 0 && input.charAt(i) == '='; i--) {
            padCount++;
        }

        return padCount <= 2;
    }

    private static boolean isBase64Char(char c) {
        return (c >= 'A' && c <= 'Z')
                || (c >= 'a' && c <= 'z')
                || (c >= '0' && c <= '9')
                || c == '+' || c == '/';
    }

    private static void usage() {
        System.out.println("Usage: please provide a mode and a string to encode/decode");
        System.exit(1);
    }
}
```

{% endraw %}

Base64 Encode Decode in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).