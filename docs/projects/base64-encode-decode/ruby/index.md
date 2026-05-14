---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-05-14
layout: default
tags:
- base64-encode-decode
- ruby
title: Base64 Encode Decode in Ruby
title1: Base64 Encode
title2: Decode in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/ruby/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

require "base64"

USAGE = "Usage: please provide a mode and a string to encode/decode"

mode, input = ARGV

abort(USAGE) if mode.nil? || input.nil? || input.strip.empty?

case mode
when "encode"
  puts Base64.strict_encode64(input)

when "decode"
  begin
    puts Base64.strict_decode64(input)
  rescue
    abort(USAGE)
  end

else
  abort(USAGE)
end

```

{% endraw %}

Base64 Encode Decode in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).