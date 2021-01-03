# Automate the Boring stuff
## Resources
- pastebin.com
- gist.github.com

## Python basics
| Operator | Operation | 
| --- | --- | 
| `**` | Exponent | 
| `%` | Modulus/Remainder | 
| `//` | Integer division/floored quotient | 
| `/` | Division | 
| `*` | Multiplication | 
| `-` | Subtraction | 
| `+` | Addition | 

Data types:  
- Integers
- Floating-point
- Strings
  - Concatenation: Operators are polyvalent. For example the addition operator when used on two string values, it joins the strings.
  - Replication: 

Functions:
- `print()`
- `input()`
- `len()`
- `str()`
- `int()`
- `float()`
- `round()`
- `abs()`

## Flow control
Diagrams:
- Start/End: Rounded rectangles
- Decision: Diamond
- Action: Rectangle

<abbr title="Named after mathematician George Boole">Boolean</abbr>:  

- `True`
- `False`


| Operator | Meaning | 
| --- | --- |
| `==` | equal to |
| `!=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

Truths tables:

And table:  

| Input | Output |
| --- | --- |
| True and True | True |
| True and False | False |
| False and True | False |
| False and False | False |

Or table:  

| Input | Output |
| --- | --- |
| True or True | True | 
| True or False | True | 
| False or True | True |
| False or False | False |

Not Table

| Input | Output |
| --- | --- |
| not True | False |
| not False | True | 


Blocks of code:  
There are three rules: 
1. Blocks begin when indentation increases
2. Blocks can contain other blocks
3. Blocks end when the indentation decreases to zero or to a containing block's indentation

While clause always consists of the following:
- The `while` keyword
- A condition, an expression that evaluates to `True` or `False`
- A colon
- Starting on the next line, an indented block of code called the `while` clause

`import` statement consist of the following:
- The `import` keyword
- The name of the module
- Optionally, more module names, as long as they are separed by commas

## Functions
A major purpose of functions is to group code that gets executed multiple times.  
In general you always want to avoid duplicating code.

When you call `print()` or `len()` function, you pass them values, called *arguments*, by typing them between the parentheses. You can also define your own functions that accept arguments.

```
def hello(name):
  print('Hello, ' + name)

hello('Alice')
hello('Bob')
```

**Parameters**: Are variables that contain arguments. When a function is called with arguments, they are stored in the parameters.  
One thing to remember is that the value stored in a parameter is forgotten when the function returns.

- **Define**: A function is to create it.
- **Call**: Executes or "calls" the function.
- **Pass**: Pass the chosen string value to the function.
- **Argument**: Is a value being passed to a function in a function call.
- **Parameter**: They are values that have arguments assigned to them.

The `None` value: Represents the absence of a value. It must be typed with a capital N.  
`sep` keyword argument  

The call stack is how Python remembers where to return the execution after each function call. The call stack isn't stored in a variable in your program; rather it creates a frame object on the top of the call stack. These objects store the line number of the original function call so that Python can remember where to return. If another function call is made, Python puts another frame object on the call stack above the other one.

When a function call returns, Python removes a frame object from the top of the stack and moves the execution to the line number stored in it.

> Note that frame objects are always added and removed from the top of the stack and not from any other place.

Local scope: Parameters and variables that are assigned in a called function
Global scope: Variables that are assigned outside all functions

When a scope is destroyed, all the values stored in the scope's variables are forgotten. 
There is only one global scope, and it is created when your program begins. When your program terminates, the global scope is destroyed, and all its variables are forgotten.  

A local scope is created whenever a function is called. Any variables assigned in the function exist within the function's local scope. When the function returns, the local scope is destroyed, and these variables are forgotten.

Scopes matter for several reasons:
- Code in the global scope, outside of all functions, cannot use any local variables
- However, code in a local scope can access global variables
- Code in a function's local scope cannot use variables in any other local scope
- You can use the same name for different variables if they are in different scopes. That is there can be a local variable named `spam` and a global variable also named `spam`.

Errors can be handled with `try` and `except` statements. When the code inside causes an error the program execution immediately moves to the code in the `except` clause. After running that code, the execution continues as normal. 

## Lists
Lists and tuples can contain multiple values.
  - List[]: Mutable value that contains multiple values in an ordered sequence, comma-delimited
    - *Index:* `list[1]`, `list[0][1]`, *Slices:* `list[2:5]`, 
    - `index()`
    - `del`
    - `enumerate()`
    - `append()`
    - `insert()`
    - `remove()`
    - `sort()` ASCII order
  - Tuple(): Immutable value that contains multiple values in an ordered sequence, comma-delimited
    - `id()`
    - `copy()` = Make a duplicate copy of a mutable value
    - `deepcopy()`= Recursive copy

## Dictionaries and structuring data
dictionary{'':''}: Unordered mutable collection of many values with a key-value pair
  - `keys()`
  - `values()`
  - `items()`
  - `get()` 
  - `setdefault()`
  - pprint: module to 'pretty printing' dictionary values
    - `pprint()`
    - `pformat()`

## Manipulating strings
Escape character: backslash(`\`) + character

| Escape character | Equivalent | 
| --- | --- | 
| `\'` | Single quote |
| `\"` | Double quote |
| `\t` | Tab |
| `\n` | Newline (line break) |
| `\\` | Backslash |

Raw string: `r` before the beginning quotation mark of a string. It ignores all escape character inside. 

An expression with two strings joined using `in` or `not` will evaluate to a Boolean `True` or `False`.

String interpolation: `%s` operator inside the string acts as a marker to be replaced by values following the string.

f-strings: Similar but braces {} are used instead of `%s`. f-prefix.

methods:
- `upper()`
- `lower()`
- `isupper()`: Returns `True` if the string has at least one letter and all uppercase
- `islower()`: Returns `True` if the string has at least one letter and all lowercase
- `isX()` methods
  - `isalpha()`: Returns `True` if the string consists only of letters and is not blank
  - `isalnum()`: Returns `True` if the string consists only of letters and numbers and is not blank
  - `isdecimal()`: Returns `True` if the string consists only of numeric characters and is not blank
  - `isspace()`: Returns `True` if the string consists only of spaces, tabs, and newlines and is not blank
  - `istitle()`: Returns `True` if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
- `startswith()`
- `endswith()`
- `join()` 
- `split()`
- `partition()`: Returns a tuple of three substrings for the "before", "separator", and "after" substrings
- `rjust(*n*)`, `ljust(*n*)`, `center(*n*)`: Return a padded version of the string they are called on, with spaces inserted to justify the text
- `strip()`: Returns a new string without any whitespace characters at the beginning or end
- `rstrip()`, `lstrip()`: Remove whitespace characters from the left and right ends, respectively
- `ord()`, `chr()`: Get the Unicode code point of a text character and viceversa

### pyperclip module
It has `copy()` and `paste()` functions that can send text to and receive text from your computer's clipboard.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Pattern matching with regular expressions

Regular Expressions, *regexes*. `re` module.

Steps:
1. Import regex module: `import re`
2. Create a `Regex` object with `re.compile()` function using a raw string.
3. Pass the needed string into `Regex` object's `search()` method. This returns a `Match` object
4. Call the `Match` object's `group()` method to return a string of the actual matched text.

methods:
- `re.compile()`
  - the following characters have special meaning: `. ^ $ * + ? { } [ ] \ | ( )
  - To detect these characters you need to escape them with a backslash
- `findall()`: returns the strings of every match in the searched string
- `search()`: returns a `Match` object of the first matched text in the searching string
- `sub()`: for `Regex` objects is passed two arguments
  - the first argument is a string to replace any matches
  - the second is the string for the regular expression
- `re.compile()` to ignore whitespace and comments inside the regular expression string
- `re.VERBOSE` as the second argument to `re.compile()` to get verbose
- `re.IGNORECASE`

- Match multiple groups: `|`, pipe match one of many expressions
- Optional matching: `?`, question mark flags the group that precedes it as an optional part of the pattern
- Match zero or more: `*`, start or asterisk 
- Match one or more: `+`, plus
- Match specific repetitions: `(){}`, braces
  - *greedy*: by default, in ambiguous situations they will match the longest string possible
  - *non-greedy*: or lazy, matches the shortest string possible, has the closing brace followed by a question mark `?`

Character classes
| Shorthand character class | Represents |
| --- | --- |
| \d | Any numeric digit from 0 to 9 |
| \D | Any character that is not a numeric digit from 0 to 9 | 
| \w | Any letter, numeric digit, or the underscore character (Matching "word" characters) |
| \W | Any character that is not a letter, numeric digit, or the underscore character | 
| \s | Any space, tab, or newline character (Matching "space" characters) | 
| \S | Any character that is not a space, tab, or newline | 

- Caret symbol `^` at the start of a regex to indicate that a match must occur at the beginning of the searched text
- Dollar symbol `$` at the end of the regex to indicate the string must end with this regex pattern
- Wildcard symbol `.` or dot will match any character except for a newline
  - To use *non-greedy* use `.*?`
  - Use `re.DOTALL` as the second argument to `re.compile()`, you can include newline character


Syntax:
- The `?` matches zero or one of the preceding group.
- The `*` matches zero or more of the preceding group.
- The `+` matches one or more of the preceding group.
- The `{n}` matches exactly n of the preceding group.
- The `{n,}` matches n or more of the preceding group.
- The `{,m}` matches 0 to m of the preceding group.
- The `{n,m}` matches at least n and at most m of the preceding group.
- `{n,m}?` or `*?` or `+?` performs a non-greedy match of the preceding group.
- `^spam` means the string must begin with spam.
- `spam$` means the string must end with spam.
- The `.` matches any character, except newline characters.
- `\d`, `\w`, and `\s` match a digit, word, or space character, respectively.
- `\D`, `\W`, and `\S` match anything except a digit, word, or space character, respectively.
- `[abc]` matches any character between the brackets (such as a, b, or c).
- `[^abc]` matches any character that isn’t between the brackets.


## Input validation
`PyInputPlus` module for input validation. Not part of python standard library.  

PyInputPlus has several functions for different kinds of input:
- `inputStr()`: Is like the built-in `input()` function but has the general PyInputPlus features. You can also pass a custom validation function to it
- `inputNum()`: Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it 
- `inputChoice()`: Ensures the user enters one of the provided choices
- `inputMenu()`: Is similar to `inputChoice()`, but provides a menu with numbered or lettered options
- `inputDatetime()`: Ensures the user enters a date and time
- `inputYesNo()`: Ensures the user enters a “yes” or “no” response
- `inputBool()`: Is similar to `inputYesNo()`, but takes a “True” or “False” response and returns a Boolean value
- `inputEmail()`: Ensures the user enters a valid email address
- `inputFilepath()`: Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists
- `inputPassword()`: Is like the built-in `input()`, but displays * characters as the user types so that passwords, or other sensitive information, aren’t displayed on the screen
- The following functions will accept `min`, `max`, `greaterThan`, and `lessThan` keyword arguments for specifying a range of valid values.
  - `inputNum()`
  - `inputInt()`
  - `inputFloat()`
- Keyword arguments:
  - `pyip.inputNum(blank=True)`: By default, blank input isn't allowed unless the `blank` keyword argument is set to `True`
  - `pyip.inputNum(limit=2)`: 
  - `pyip.inputNum(timeout=20)`: 
  - `pyip.inputNum(timeout=20, default='N/A)`: 
  - `pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])`: The function will accept Roman numerals
  - `pyip.inputNum(blockRegexes=[r'[02468]$])`: The function won't accept even numbers
    - If you specify both an `allowRegexes` and `blockRegexes` argument, the allow list overrides the block list.


## Reading and writing files
To make scripts working on every OS is strongly suggested to write paths using double backslash `\\`. Ex. (`'C:\\delicious\\walnut\\waffles')

- `import os`
  - `mkdir()`: Makes one directory at a time
  - `os.makedirs()`: Makes more directories at once
- `from pathlib import Path`: Introduced in Python 3.4 to replace older some `os.path` functions
- `Path.cwd()`: Get current working directory as a string
  - *old_way* `os.getcwd()`
- `os.chdir()`: call directory
- `os.path()`: Gets a path
  - os.path.abspath(*path*): Returns a string of the absolute path of the argument. 
  - os.path.isabs(*path*): Returns `True` if the argument is an absolute path and `False` if it is a relative path
  - os.path.relpath(*path*, *start*): Returns a string of a relative path fro the `start` path to `path`. If start is not provided, the cwd is used as a path

Given a `path` object, you can extract the file's path different parts as strings using several `Path` object attributes:
- Anchor: Root folder of the filesystem
- Drive: On windows is the single capital letter that denotes a storage device
- Parent: Folder that contains the file
- Name: Made up of the *stem* or *base name* and the *suffix* or *extension*

> Note: Windows `Path` objects have a `drive` attribute while macOS and Linux `Path` objects don't

Path: path objects
- `.anchor`: 
- `.parent`: 
- `.name`: 
- `.stem`: 
- `.suffix`: 
- `.drive`: 
The `parents` attribute, different from `parent` attribute, can be walked with an integer index:
```
>>> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
>>> Path.cwd().parents[0]
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
>>> Path.cwd().parents[1]
WindowsPath('C:/Users/Al/AppData/Local/Programs')
>>> Path.cwd().parents[2]
WindowsPath('C:/Users/Al/AppData/Local')
>>> Path.cwd().parents[3]
WindowsPath('C:/Users/Al/AppData')
>>> Path.cwd().parents[4]
WindowsPath('C:/Users/Al')
>>> Path.cwd().parents[5]
WindowsPath('C:/Users')
>>> Path.cwd().parents[6]
WindowsPath('C:/')
```
older `os` module version:

- `os.path.dirname()`: 
- `os.path.dirname()`: 
- `os.path.split()`: Does not take a file path and return a list of strings of each folder
  - `split(os.sep)`: Is used to return a list of strings of each folder 

File operations:
- `os.path.getsize(*path*)`: Returns the size in bytes
- `os.listdir(*path*)`: Returns a list of filename strins for each file

- `glob()`: Glob patterns are simplified Regex. Returns a generator object


- `p.exists()`: Returns `True` if the path exists or returns `False` if it doesn’t exist.
- `p.is_file()`: Returns `True` if the path exists and is a file, or returns `False` otherwise.
- `p.is_dir()`: Returns `True` if the path exists and is a directory, or returns `False` otherwise.


- `write_text()`: Creates a new text file or overwrites an existing one with the string passed to it.

There are three steps to reading or writing files:
- `open()`: Returns a `File` object.
- `read()` or `write()`
  > Write() does not automatically add a newline character to the end of the string
  - `readlines()`: Returns a list of string values from the file, one for each line of text.
    > Except for the last line of the file, each of the string values ends with a newline character \n.
    > A list of strings is often easier to work with than a single large string value.
- `close()` 


You can save variables in your Python programs to binary shelf files using `shelve` module. This way, your program can restore data to variables from the hard drive.
```
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```

Saving variables with `pprint.pformat()` function. It gives a string that can be written to a `.py` file making your very own module.


- The benefit of creating a `.py` file, opposed to saving variables with the `shelve` module, is that because it is a text file, it can be read and modified by anyone with a simple text editor.

Project:  Updatable Multi-Clipboard

## Organizing files

`shutil` or shell utilities module has functions to copy, move, rename and delete files in your Python programs.
  - `shutil.copy(*source*, *destination*)`: Will copy a single file.
  - `shutil.copytree(*source*, *destination*)`: Will copy an entire folder and every folder and file contained in it.
  - `shutil.move(*source*, *destination*)`: Will move the file or folder. It will overwrite homonyms.
    - If it doesn't find the folder name you are moving it to it assumes it is the new name of the file. 
    - Always check if the folder exists to avoid problems
- `os.unlink(*path*)`: Will delete the file at *path*
- `os.rmdir(*path*)`: Will delete the folder at *path*. This folder must be empty of any files or folders.
- `shutil.rmtree(*path*)`: Will remove the folder at *path*, and all files and folders it contains will also be deleted.
  - Double check before deleting
- `send2trash`: Module that can only send files to the recycle bin.
- `os.walk`: 
  - Returns three values on each iteration through the loop
    - A string of the current folder's name
    - A list of strings of the folders in the current folder
    - A list of strings of the files in the current folder
- `zipfile`: 
  - `.extractall()`: Extracts all the files and folders 


- ``: 
- ``: 

## Debugging
## Web scraping
## Working with excel spreadsheets
## Working with google sheets
## Working with pdf and word documents
## Working with csv files and json data
## Keeping time, scheduling tasks and launching programs
## Sending email and text messages
## Manipulating images
## Controlling the keyboard and mouse with GUI automation
