# Contributing

## Table of Contents

- [Contributing](#contributing)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Issues](#issues)
    - [Pull Requests](#pull-requests)
  - [Articles](#articles)
    - [General Guidelines](#general-guidelines)
    - [Sample Program Article](#sample-program-article)
      - [how-to-implement-the-solution.md (manditory)](#how-to-implement-the-solutionmd-manditory)
      - [how-to-run-the-solution.md (manditory)](#how-to-run-the-solutionmd-manditory)
    - [Language Article](#language-article)
      - [description.md (manditory)](#descriptionmd-manditory)
  - [Images](#images)
    - [General Guidelines](#general-guidelines-1)
    - [Title Image](#title-image)
    - [Other Images](#other-images)
      - [Local Images](#local-images)
      - [External Images](#external-images)
  - [Building Website Locally](#building-website-locally)

## Overview

Any issues or pull requests must adhere to the guidelines below. Any that do not will be closed.
You will find more detail about each guideline throughout the rest of this document.

### Issues

Before making a pull request, please create one of the following issues:

- [Sample Program Article][1]
- [Language Article][2]

### Pull Requests

Please make sure that your pull request follows these guidelines:

- There is a corresponding issue.
- For a sample program article, there is a corresponding stub. This stub is auto-generated by the
  website automation and is in ``https://sampleprograms.io/projects/<project-name>/<language>/``.
  For example, https://sampleprograms.io/projects/baklava/ada/. You can tell that this is a stub
  because the "How to Implement the Solution" and "How to Run the Solution" sections indicates
  that the section is not available. For more information on how to write a sample program article,
  see [this](#general-guidelines) and [this](#sample-program-article).
- For a language article, there is a corresponding stub. This stub is auto-generated by the
  website automation and is in ``https://sampleprograms.io/languages/<language>/``.
  For example, https://sampleprograms.io/languages/ada/. You can tell that this is a stub because
  the "Description" section indicates that the section is not available. For more information on
  how to write a language article, see [this](#general-guidelines) and [this](#language-article).
- The [Website Automation][3] passes.

## Articles

### General Guidelines

Please make sure that your article follows these guidelines:

- All articles go in folders under `sources` folder, **not** the `docs` folder. The `docs` folder
  is used to generate the website.
- All articles are written using Markdown. If you are unfamiliar with this, please refer to
  [this guide][5].
- If you use someone else's work, please cite your references.
- If your article requires multiple files (such as a sample program article) and you use
  numbered references, the numbers *must* be unique\. For example, you have this for your last
  numbered reference in the first file:

  ```markdown
  [11]: https://www.gnu.org/software/make/manual/html_node/Make-Control-Functions.html#index-info
  ```

  and you have this for your first numbered reference in the last file:

  ```markdown
  [12]: https://leangaurav.medium.com/how-to-setup-install-gnu-make-on-windows-324480f1da69
  ```

- If your article has multiple sections, they *must* start at level 3. For example:

  ```markdown
  ### Setup

  ...

  ### Input Validation

  ...
  ```

### Sample Program Article

A sample program article describes an existing sample program in the [Sample Programs][4]
repository.

Files for this article are placed in the `sources/programs/<project>/<language>` folder, where:

- `<project>` is the project name in lowercase, with spaces converted to dashes. For example,
  `binary-search` for the "Binary Search" project.
- `<language>` is the language name in lowercase, with spaces converted to dashes, and symbols
  like `+` converted to words. Examples:
  - `c-plus-plus` for `C++`
  - `c-sharp` for `C#`
  - `google-apps-script` for `Google Apps Script`

This folder must be created. The next sections describe the files that go into this folder.
Images go into the same folder. These are optional. See [Images](#images) for details.

#### how-to-implement-the-solution.md (manditory)

This file contains a description of how the sample program works. There is no need to copy/paste
in the entire program into this file; that is automatically done by the website automation.
Instead, you may show portions of the code with explanations around them. The code is enclosed in
triple-backticks followed by the language name (use the same name as `<language>` shown above).
For example, here is a description of a portion of code written in Go:

<pre>
Breaking down this solution bottom up,
```go
func main() {
    if len(os.Args) != 2 {
        exitWithError()
    }

    nums := strToSliceInt(os.Args[1])
    nums = bubbleSort(nums)
    fmt.Println(sliceIntToString(nums))<br>
}
```
This is the `main` function of this file. It parses ...
</pre>

#### how-to-run-the-solution.md (manditory)

This file contains instructions on how to run the sample program. It should contain the following:

* Instructions on how to download and install the programming language.
* What commands are needed to build (if applicable) and execute the code.

Alternatively, you can document how to use an online tool that can be used to run the code.
For example, [programviz.com has an online C++ compiler][6] into which you can copy/paste the
sample program and run it.

### Language Article

A language article describes an existing language in the [Sample Programs][4] repository.

Files for this article are placed in the `sources/languages/<language>` folder, where:

- `<language>` is the language name in lowercase, with spaces converted to dashes, and symbols
  like `+` converted to words. Examples:
  - `c-plus-plus` for `C++`
  - `c-sharp` for `C#`
  - `google-apps-script` for `Google Apps Script`

This folder must be created. The next sections describe the files that go into this folder.
Images go into the same folder. These are optional. See [Images](#images) for details.

#### description.md (manditory)

This file contains a description of a programming language. It should contain enough detail
to give an overview of the language. It may contain snippets of code with explanations around
them. The code is enclosed in triple-backticks followed by the language name (use the same name as
`<language>` shown above). For example, here is a description of a portion of code written in D:

<pre>
Perhaps the most interesting feature to me has to be the inline 
assembler. Apparently, developers can write assembly code directly 
in D source code:

```d
void *pc;
asm
{
    pop  EBX;
    mov  pc[EBP], EBX;
}
```
</pre>

## Images

Images may be one of the following (unless otherwise noted):

* Images stored in the same folder as the article. Let's call these local images.
* External images that are referenced by their URL.

### General Guidelines

Please make sure that your images follow these guidelines:

- Do *not* use copyrighted images, images that require royalty payments, or any non-free images.
- Do *not* use images that have watermarks on them. That is usually an indication that the image
  has usage conditions that are incompatible with this site.
- Do *not* use images or sites (for external images) that violate the [Code of Conduct][7].
- For external images, these *must* come from free sites that do not require a login.
- If an image requires an attribution, this *must* be added somewhere in the article, preferrably
  close to the image in question.
- Images must be in one of the following formats:
  - JPEG (`.jpg`)
  - PNG (`.png`)
  - GIF (`.gif`)

Here are some good sources for free, non-copyrighted local images:
  - https://pixabay.com/
  - https://www.pexels.com/

### Title Image

This image is placed at the top of articles. This *must* be a local image, and the file name
*must* be one of the following:

- `featured-image.jpg`
- `featured-image.png`
- `featured-image.gif`

Please do not use any animated GIFs for this. The recommended size is 1200x628. The image is
modified by [image-titler][8] which handles resizing, cropping, and decorating the image with the
[logo][9], and that size works best. The website code itself handles adding the image title.

If this image is not used, then a default image is used. For sample program articles, this is the
same image as the project:

- Navigator to [here][10].
- Click on the project.

For language articles, [this][11] is the default image.

### Other Images

Other images may be added to your articles to help clarify key points more clearly than words
alone.

#### Local Images

Local images are referenced like this:

```markdown
![Name of image](<image-directory>/<image-filename>)
```

where `<image-directory>` is one of the following directories, and `<image-filename>`
is the filename of the image:

* Sample program article: `/assets/images/projects/<language>/<project>`
* Language article: `/assets/images/languages/<language>`

For example:

```markdown
![Annotated Baklava in Piet](/assets/images/projects/baklava/piet/baklava-annotated.png)
```

#### External Images

External images are referenced like this:

```markdown
![Name of image](<url>)
```

where `<url>` is the website to the image. For example:

```markdown
![Example Graph](https://media.geeksforgeeks.org/wp-content/uploads/20210727035309/UntitledDiagram92.png)
```

## Building Website Locally

Prerequisites:

* [Python 3.9 or better][12]
* [pip python package][16]
* [virtualenv python package][13]
* [poetry 2.1.1 or better][15]
* [Docker][14]

If you wish to build a local copy of the website install the necessary packages:

```console
poetry install
```

You should only need to do the above once. All other times, just activate the virtualenv with the
`source` command.

Now, run `./generate.sh`. This will build the website, create a temporary web server, and open
up the home webpage in your default browser at `http://localhost:8000/index.html`. When you are done,
just press Ctrl+C to exit the web server.

[1]: https://github.com/TheRenegadeCoder/sample-programs-website/issues/new?assignees=&labels=sample+program&projects=&template=sample-program-article-request.md&title=Add+%5BSample+Program%5D+in+%5BLanguage%5D+Article
[2]: https://github.com/TheRenegadeCoder/sample-programs-website/issues/new?assignees=&labels=language&projects=&template=language-article-request.md&title=Add+%5BLanguage%5D+Language+Article
[3]: https://github.com/TheRenegadeCoder/sample-programs-website/actions/workflows/main.yml
[4]: https://github.com/TheRenegadeCoder/sample-programs
[5]: https://www.markdownguide.org/basic-syntax/
[6]: https://www.programiz.com/cpp-programming/online-compiler/
[7]: https://github.com/TheRenegadeCoder/sample-programs-website/blob/main/.github/CODE_OF_CONDUCT.md
[8]: https://github.com/TheRenegadeCoder/image-titler
[9]: https://github.com/TheRenegadeCoder/image-titler/blob/main/imagetitler/assets/icons/the-renegade-coder-sample-icon.png
[10]: https://sampleprograms.io/projects/
[11]: https://github.com/TheRenegadeCoder/sample-programs-website/blob/main/sources/languages/featured-image.jpg
[12]: https://www.python.org/downloads/
[13]: https://pypi.org/project/virtualenv/
[14]: https://docs.docker.com/engine/install/
[15]: https://pypi.org/project/poetry/
[16]: https://pypi.org/project/pip/
