As we can see, reversing a string in Swift is pretty short and sweet. At this
point, let's dig into the code a bit.

### Foundation

On line 1 of our sample code, we import [Foundation][1]:

```swift
import Foundation
```

`Foundation` is a framework that contains many basic data types. This framework
also bridges between Swift types, such as `String`, and Objective-C types, such
as [NSString][2]. When you import almost any of Apple's Swift frameworks, you are
implicitly importing Foundation along with them.

### Guard

The guard statement on line 3 is one of Swift's many syntax features which favor
safety and human readability:

```swift
guard CommandLine.argc > 1 else {
  exit(0)
}
```

A [guard statement][3] is a conditional that only fires off if something isn't true.
This is good for highlighting error conditions, and prevents code from becoming
littered with nested if-else statements. It is especially powerful when dealing
with Swift's Optionals.

### CommandLine

`Commandline.arguments` is a built-in way to access user input:

```swift
let usersString = CommandLine.arguments[1]
```

Because `CommandLine.arguments` is a `String` array, not an `Optional`, we check its
length, rather than look for `nil`, in order to see if the user has passed us any
input. In Swift, only `Optional`s can contain `nil`.

Furthermore, `CommandLine.arguments` is always initialized with at least one thing
inside it: the path of the particular file the code is stored in. Therefore, to
access user input, we check if the array contains more than one `String`. Then we
call the `String` at the second index; the first index will always contain the path.

Finally, `CommandLine` has a special property, `.argc`, which allows us to know how
many `String`s are inside `Commandline.arguments`. We could also call `.length` on
`Commandline.arguments` to access this information. This is the usual way we access
the number of things in an array, but here we use `.argc` to highlight a unique
feature of working with `CommandLine`.

### String

When we reverse a `String` in many languages, we may opt for the manual way, by
looping over each character. Instead, we can reverse the string directly through
a builtin call:

```swift
let reversedCollection = usersString.reversed()
```

Swift has an unusual approach to `String`s. Swift stores all characters in `String`s
as Unicode, even if they are within the ASCII character set. Therefore, we don't
need to do anything funky to cover all our edge cases: Swift can innately handle
accented characters, Cyrillic, kanji, and so on.

While this allows Swift to seamlessly handle emoji and languages that use
non-English characters, it can make working with `String`s a bit more complicated.

Swift's `String` API has changed frequently from version to version, as Apple
continually tries to balance universal language support with ease of use. In
early versions, Swift `String`s were more like Javascript's `String` implementation,
where `String`s were not quite arrays, but you could still call a specific
character by indexing into it with an integer value.

As of Swift 4, `String`s are composed of a special kind of character collection,
quite distinct from arrays. Indexing into a `String` is done via special methods
and indexing objects specific to the task. This makes looping over all of the
characters in a `String` a more difficult task than in other languages.

Thankfully, we do not have to resort to this to reverse a String , we can simply
call the `.reversed()` method (or `.reverse()`, in earlier Swift versions).

### Reversed()

The `.reversed()` method does not mutate the original `String`, nor does it return a
new `String`. Instead, it works over the character collection making up our `String`,
and we get back an instance of `ReversedCollection`, an incompatible type. This
forces us to be more precise about what we intend to do with our return values.
Later, we use our `ReversedCollection` to make a new `String` object:

```swift
let reversedString = String(reversedCollection)
```

Fortunately, we can perform a quick cast to get our reversed string.

### Print

Finally, on line 11, we come to a nice, straight-forward print statement:

```swift
print(reversedString)
```

Unlike other languages, we don't need to specify the console. The compiler
implicitly knows. Apple also offers a logging system, for more robust results
when debugging.

[1]: https://developer.apple.com/documentation/foundation
[2]: https://developer.apple.com/documentation/foundation/nsstring
[3]: https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Guard-Statement
