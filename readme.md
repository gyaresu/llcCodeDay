# Ladies Learning Code - National Code Day

### PyCharm comes built-in with an older version of Python

This is just a quick follow up to a couple of issues you might have with the examples in `llc-intro-to-python-master` or the [PyCharm Edu tutorial][pc]

The latest version of [PyCharm Edu][pc] uses Python Version: `2.6.9 (unknown, Jul 14 2015, 19:46:31) `

You can see that by importing the system library (in any of the PyCharm `.py` files) and printing the version, as such:

```python
import sys
print(sys.version)
```

This lead to the exercise reference code `writing_csv.py` to give me the error below:

```python
Traceback (most recent call last):
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)]
  File "/Users/gyaresu/programming/llc-intro-to-python-master/exercises/writing-example.py", line 24, in <module>
  <type 'file'>
      filtered_writer.writeheader()
      AttributeError: DictWriter instance has no attribute 'writeheader'
      
      Process finished with exit code 1
```

If I just run the file from a terminal (iTerm/PuTTY/whatever) then it's successful because system Python is version `2.7.10` which has the `Dictwriter.writeheader` that we need.

```bash
$ python -V
Python 2.7.10
```


If none of this makes sense let me know here as a comment or via Twitter and I'll help you out.

Have a look at https://github.com/gyaresu/python-stuff/blob/master/filter-csv.py for a solution using `"with open"`. 

`with open` automatically closes the file for you but as you'll see in my code you have to 'nest' the write file inside the readfile block because outside of that block the file is closed(!)

### PyCharm built-in Tutorial

I _highly_ recommend doing the build-in tutorial that comes with PyCharm. It's fun and guides you through the problems.

What I did find though was the problem `Introduction to Python` > `Strings` > `Character Escaping` can seem to be completed successfully but then not pass the test.

I found the solution at this Stack Overflow question: [Print out text using one String in Python [closed]][so]

Again, if you're confused by this please reach out via Twitter or comment here.

[pc]:       https://www.jetbrains.com/pycharm-edu
[so]:       http://stackoverflow.com/questions/27464503/print-out-text-using-one-string-in-python
