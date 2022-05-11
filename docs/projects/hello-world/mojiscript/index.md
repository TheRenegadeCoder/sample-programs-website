---

title: Hello World in Mojiscript
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Hello World in Mojiscript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mojiscript
import log from 'mojiscript/console/log'
import pipe from 'mojiscript/core/pipe'
import run from 'mojiscript/core/run'

const state = 'Hello, World!'

const main = pipe ([
  log
])

run ({ state, main })
```

{% endraw %}

Hello World in Mojiscript was written by:

- Noah Nichols
- Patrick Biffle

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 17 2018 11:30:32. The solution was first committed on Oct 15 2018 16:02:18. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).