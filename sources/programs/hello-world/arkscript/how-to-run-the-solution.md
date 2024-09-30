Using the online playground:

1. Go to [playground.arkscript-lang.dev](https://playground.arkscript-lang.dev/#/pages/ide/ark/hello_world.template)
2. Copy the code you want to run, eg `(print "Hello, World!")`, and paste it in the editor
3. Click the `Run` button

Using the interpreter:

1. Download the [latest release](https://github.com/ArkScript-lang/Ark/releases)
  1. See [the documentation](https://arkscript-lang.dev/tutorials/building.html#from-a-release) in case you need help finding the correct binary & installing it
2. Create a `file.ark` with your code inside
3. Run it using `arkscript file.ark`

Using Docker:

1. Pull `arkscript/nightly:latest`
2. Create a `file.ark` with your code inside
3. Run it using `docker run --rm -v $(pwd):/tmp arkscript/nightly /tmp/file.ark`

