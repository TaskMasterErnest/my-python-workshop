# Executing Programs, Algorithms and Functions
Apparently by the end of this session, I would be able to do the following:
- write and execute Python scripts from the command line
- write and import Python modules
- document code with docstrings
- implement basic algorithms
- write functions with dynamic programming algorithms
- modularize code
- write helper and lambda functions

## Scripts and Modules
A script is designed to be executed from the command line. It is a standalone file that contains Python logic to be executed.

A module is Python logic that is designed specifically to be imported into a script.

Functions are bits of code that present a specific logic. In code in which I wish to read and write to a file, I can have a function to handle the reading and another to handle the writing; then I can use these in my main logic and call them as I wish.

Functions in Python are introduced with the `def` keyword, followed by the name of function then the input of the function in parentheses...all just before a colon. eg. `def eat(food):`.
```Python
def triple(number):
  result = number * 3
  return result

# call function
triple(5)
```

It is important to specify here the Python script should run. Most importantly on Linux machines. To be on the safe side, you can start Python scripts with a shebang (`#!`).
- start Python scripts with `#!/usr/bin/env python3`.

Libraries, classes, modules and functions can be imported into Python code. Here are some ways to import libraries in Python:
- import the library and use it with a method to get the desired result - `import math; math.exp(2)`.
- import the specific method from the library - `from math import exp; exp(2)`.
- import everything from the library; usually not adviced - `from math import *`.
- as an aside, we can import the library and method with a preferred name - `from math import exp as exponential; exponential(2)`.

The dreaded `if __name__ == '__main__` statement I see in most Python code. THis is used when you want to execute a Python scrit by itself, or, you want to import objects from the script as if it was a module.
- to do this, you write the code such that the object you eventually want to export/import somewhere else is after ths statement.
```Python
# a function that adds numbers from 1 - 10 only
result = 0
for n in range (1, 11):
  result += n
print(result)

# using the statement
result = 0
for n in range(1, 11):
  result += n

if __name == '__main__':
  print(result)
```
- with the last code block above, I can import the result into another code block and use it.

## What is an algorithm?
An algorithm is a set of instructions that are to be/are executed in a certain manner to perform a certain task.
- prepping cereal is an algorithm - milk first or cereal first?? (now this is an algorithm worthy of standardizing).

Express algorithms in `pseudocode` so you and everyone else can understand what task you wish to perform and in what order.
- Psudocode is just a words the task you want to achieve and the steps to achieve them (often in plain language/English).

Psuedocode helps to clear your thought process and also helps anyone not familiar with the code to understand what you intenc to achieve.

### The Time Complexity thing
What is this time complexity thing that everyone is talking about?
- Pairing the knowledge we have from algorithms, time complexity can be said to be the relationship between the size of a problem to solve and the steps taken to solve this problem.

This time complexity thing is used when we cannot directly measure the time it will take to solve a problem of a particular size. Eg. I have a big bowl of jollof with assorted meat (a delicacy where I come from). I cannot accurately compute the time it will take for me to eat all that; maybe I might not finish eating it at all.

The time complexity is not a satisfactory measurement tool either because there are factors that it does not know and cannot accurately model (from the start) to solve the problem. Eg. in computers - the memory, processor, disk-speed etc so time complexity ends up depending on the computer used to solve the problem.
- in jollof-eating terms, I cannot accurately state the time to finish eating the jollof as it depends on the size of the bowl, the size of my scooping tool, how fast I can eat, how spicy the food is, the food's temperature etc.

Instead, what we can effectively do is to count the number of steps taken to execute the algorithm. The result of this counting is expressed as the big-O notation.
- in jollof terms, we count the number of scoops it will take to finish the big bowl of jollof and tthis becomes the yardstack by which we judge all people eating jollof.

There is a big-O notation thing called O(n) which means that for a problem of size 'n', the number of steps to be taken to solve it should be proportional to 'n'.
- mathematically, it is expressed in some fancy terms as (a * n + B), where a and B are contants.
- this simply means that, the steps needed to execute a program/algorithm grow linearly with the problem size. The bigger the problem size, with things kept constant, the more steps to be taken to solve the problem.
- in jollof terms, an even bigger serving of jollof, if we keep the spoon size and bowl size constant, will require even more scoops to be taken in order to finish eating the jollof.