---

title: Baklava in Swift
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Baklava in Swift page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Swift
func baklava(maxWidth: Int) -> Void {
    for number in 0...maxWidth {
        print(String(repeatElement(" ", count:maxWidth-number)) + String(repeatElement("*", count:number*2+1)))
    }
    for number in (0...maxWidth-1).reversed() {
        print(String(repeatElement(" ", count:maxWidth-number)) + String(repeatElement("*", count:number*2+1)))
    }
}
baklava(maxWidth: 10)
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).