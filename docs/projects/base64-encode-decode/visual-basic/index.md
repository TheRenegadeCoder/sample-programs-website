---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-05-07
layout: default
tags:
- base64-encode-decode
- visual-basic
title: Base64 Encode Decode in Visual Basic
title1: Base64 Encode Decode
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/visual-basic/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System.Text

Module Program

    Sub Main(args As String())

        If args.Length <> 2 Then
            ShowUsage()
            Return
        End If

        Dim mode = args(0).ToLowerInvariant()
        Dim value = args(1)

        If String.IsNullOrWhiteSpace(mode) OrElse String.IsNullOrWhiteSpace(value) Then
            ShowUsage()
            Return
        End If

        Select Case mode

            Case "encode"
                Console.WriteLine(
                    Convert.ToBase64String(
                        Encoding.UTF8.GetBytes(value)
                    )
                )

            Case "decode"
                Try
                    Console.WriteLine(
                        Encoding.UTF8.GetString(
                            Convert.FromBase64String(value)
                        )
                    )

                Catch ex As FormatException
                    ShowUsage()
                End Try

            Case Else
                ShowUsage()

        End Select

    End Sub

    Private Sub ShowUsage()
        Console.WriteLine("Usage: please provide a mode and a string to encode/decode")
    End Sub

End Module
```

{% endraw %}

Base64 Encode Decode in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).