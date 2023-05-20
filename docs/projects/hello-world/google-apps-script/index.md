---
title: Hello World in Google Apps Script
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-google-apps-script.jpg
tags: [google-apps-script, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Google Apps Script](https://sampleprograms.io/languages/google-apps-script) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```google_apps_script
function helloWorld() {
  Logger.log("Hello, World!");
}
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Google Apps Script](https://sampleprograms.io/languages/google-apps-script) was written by:

- Arun Pattni
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2018 14:58:56. The solution was first committed on May 09 2018 19:50:32. As a result, documentation below may be outdated.

## How to Implement the Solution

Unlike many languages, Google Apps Script code doesn't need a `main` function. In fact, all we have to do is define a function. Google handles what we want to do with the script at runtime.

With that in mind, we can see that we've defined a helloWorld function with syntax similar to [JavaScript][1]. In other words, we have a function definition which encloses a code block with braces.

Inside the code block, we have our typical print call. In this case, we leverage the `Logger` to do our printing. Then we pass our "Hello, World!" string to the log function, and call it a day.

[1]: https://en.wikipedia.org/wiki/JavaScript


## How to Run the Solution

If we want to run Hello World in Google Apps Script, we actually have to write our scripts using the [Apps Script tool][2]. From there, [Google has some nice documentation][3] for running them.

Alternatively, we can write scripts locally and upload them to Google Drive. At that point, we can connect the Google Apps Script tool to run our scripts. The link above has directions for that option as well.

If you know of other ways to run Google Apps Script code, let me know in the comments.

[2]: https://developers.google.com/apps-script/guides/clasp
[3]: https://developers.google.com/apps-script
