# WHY AM I DOING THIS?
Unfortunately, I have the pleasure of being enrolled in a bootcamp where I have to learn Python to produce scripts to work on a task in, wait for it, ... 3 days. 

I must say I am not the least bit thrilled cos I touched on this language 4-5 years ago and never went back. And now I have to learn this over the weekend ASAP.

I am using a really good workshop book that promises not to take me from zero to hero but will make me appreciate the language and apply it much better.

Once again, I am not the least bit thrilled at the amount of time I have to use to get confortable with this language aagain but I hope things will turn out for the best this time around.

sigh :\

## Calculator
Writing a program to perform the basic math operations we love and know.

| Operation | Symbol |
| --------- | ------ |
| Addition | + |
| Subtraction | - |
| Multiplication | * |
| Division | / |
| Integer Division | // |
| Exponentiation | ** |
| Modulo/Remainder | % |

You determine the type of a number using the `type` keyword.

When working with complex numbers, Python uses `j` instead of `i`. ie complex number = 2 + 5j.

Get the important kwywords from Python using this:
```Python
import keyword
print(keyword.kwlist)
```

Comments are preceeded with #
Docstrings, which contain more comments across multiple lines are enclosed in `""" """`.
Check out the `pythagorean-theorem.py` code.

Strings are placed in single or double quotes. By preference, I gravitate towards double quotes.
- For multi-line strings, use triple quotes (`'''`). They are similar to docstrings but are different as docstrings appear at the beginning and multi-line strings appear in code.

String concatenation - fancy word for joining is used to string together differnet strings (pun intended).
- We use the + operator to join a string to another. The * operator is used to repeat a string by a specified numebr of times.

String interpolation is the injection of the value of a variable into an output. The two methods to do this are by comma separation and using format.
- comma separators - inject the value from variable by specifying the cariable using commas. 
greeting = "Ciao"
print("Should we greet people with", greeting, "in this parts?")
- format - also converts python types to strings upon execution. It uses curly brackets and dot notation.
age = 74
name = taskmaster
print("The owner of this repo's name is {}. He should be {} years old by now." .format(name, age))

Use the len() function to get the length / number of character present in a set. Blank spaces are also counted.

Use the input() to get data from user interactively. 

Indexing is used to the position of data. It is ordered from 0...

Slicing is taking a subset of a string or a set of items.
- slicing is done with the (:) character. done this way = [n:m]. To get the subset of the first n stuff, [:n]; get the subsequent subset of stuff, [n:]

Using boolean and logical operators. Boolean values are True or False.
- using logical operators; and, or and not.
- And is true when both parties are true; Not negates the value; Or is true if either party is true.

Comparing string in Python makes no sense at first, till you discover that it is based on the alphabetical order of the letter in the string. 
- "a" < "c" is True because C comes after A, making it 'more'. "Accra" > "Lagos" is False because L is of a higher order number than A.

Conditionals are used to execute a set of code when a certain condition is met.
- the if syntax is the most used.
- the if-else syntax too 
- and the elif syntax, that sits between the if and else.

Indentation is important in Python, use it!

Loops are used to go round and round over the same thing until a certain condiion is met.
- while loops are the worst culprit, use with care. Best to ALWAYS remember to use an incrementor to 'decrementor' when using these.
- use break to immediately terminate a loop once a certain condition has been met. Example below uses this and double indentation.
```python
x = 10
while x <= 1000:
  x += 1
  if x % 17 == 0:
    print("{} is the first number to be divisible by 17".format(x))
```
- for loops are like while loops but they have the added advantage of being able to iterate over almost all types.
  - use for with range and and loop over the items specified in a "set".
- continue is like break but this one stops the loop and starts from the beginning of the loop again.