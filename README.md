# Sample Programs in Every Language Website

[![Discord](https://img.shields.io/discord/612072397545275424)](https://discord.gg/Jhmtj7Z)  

Welcome to the Sample Programs in Every Language Website repository. Here, the documentation
for all the code snippets is maintained. 

If you'd like to contribute, you're welcome to make any additions or changes you like
to the source files (see sources folder). These files are used to automatically
generate the documentation.

See our list of issues to get started or create your own!

[language-template]: https://github.com/TheRenegadeCoder/sample-programs-website/blob/master/templates/LANGUAGE_ARTICLE_TEMPLATE.md
[project-template]: https://github.com/TheRenegadeCoder/sample-programs-website/blob/master/templates/PROJECT_ARTICLE_TEMPLATE.md
[sample-program-template]: https://github.com/TheRenegadeCoder/sample-programs-website/blob/master/templates/CODE_ARTICLE_TEMPLATE.md
[image-titler]: https://github.com/TheRenegadeCoder/image-titler

## Building Website Locally

If you wish to build a local copy of the website, create a virtualenv, activate it, and install
`requirements.txt`:

```console
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

You should only need to do the above once. All other times, just activate the virtualenv with the
`source` command.

Now, run `generate.sh`. This will build the website, create a temporary web server, and open
up the home webpage in your default browser at `http://localhost:8000/index.html`. When you are done,
just press Ctrl+C to exit the web server.

## Where to Put Images

Images for articles that are suppose to be modified by [image-titler][image-titler] should be
placed in `sources/images`. The filename should look like this:

```
<project>-in-<language>.<extension>
```

where:

- `<project>` is the name of the project in lowercase, with spaces converted to dashes.
  For example: `even-odd` for `Even Odd`
- `<language>` is the name of the language in lowercase, with spaces converted to dashes,
  and symbols like `+` converted to words. Examples:
  - `c-plus-plus` for `C++`
  - `c-sharp` for `C#`
  - `google-apps-script` for `Google Apps Script`
- `<extension>` is the image file extension, such as `jpg`, `png`, etc.

All other images are stored in the following directories:

- Project: `docs/assets/projects/<project>`
- Language: `docs/assets/languages/<language>`
- Sample Program: `docs/assets/projects/<project>/<language>`

In the article, you can reference these like this:

```markdown
![Name of image](<image-directory>/<image-filename>)
```

where `<image-directory>` is the directory where the image is stored without `docs`.
For example:

```markdown
![Space Loop 1](/assets/images/projects/baklava/piet/space-loop1.png)
```
