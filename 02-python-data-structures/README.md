# Data Structures in Python
I have made it this far. Onwards to the second topic in Python. Data Structures. 
Why am I doing this again? It is to get into the DevOps space with knowledge in Python.

I have seen it used soo many times and now I am in a bind, so this career driven-development right here.

Let's Go! (Golang..I miss you, I will be back soon.)

## Data Strutures fr fr
Data structures refer to objects that are used to store data / hold some data together. The data stored is usually a collection of related stuff.

There are 4 main data structures in Python: lists, dictionaries, tuples and sets.

The data structures define the relationship between the data and operations that can be performed on these data. 
- they are a ways of arganizing and storing data that can be accessed efficiently under different circumstances.

## Lists
List is a container for storing multiple data sets at the same time.
- compared to arrays in other languages, but can do so much more.
- written in square brackets `[]`.
- each element has its own position and index. and indexing starts from 0 (remember this.)
- contain items, these can be iterated over using a for loop.
- allow for mutiple data types to be put on the same list. You can put strings, int and boolean all on the same list

Store lists in lists, these are called nested lists. And this can be used to represent a complex data structure.

Table data is the way most data is presented to our code but it is not the job of the programming language.
- Nested lists are treated like matrices. They have rows and columns athat contain data that can be iterated over.
- look at the `nested-list.py` file to gain some insight.
- check out the `nested-employee-data.py` file for some beautiful code on presenting data.

Some matrix data operations test is done in `matrix-operations.py` and `matrix-multiplication.py`

Here are some of the methods used with lists: slicing, sorting, appending, searching, inserting and removing.


## Dictionaries
A dictionary is an unordered collection of data stored in values and accessed by keys.
- written in `{}` curly braces as opposed to lists
- looks like JSON
- dictionaries and lists share these:
  - can be used to store values
  - updated in place; can grow and shrink on demand.
  - can be nested. dictionary can contain another dictionary; list can contain list; list can contain dictionary and dictionary can contain list.
- they differ in this way:
  - lists are accessed by positional indexes
  - dictionaries are accessed by keys
- rules to remember when using dictionaries
  - keys must be unique; no duplicate keys
  - keys must be immutable - tuple, string or number.

Database can be a List; a Record in database can be represented as a Dictionary.

>> I upgraded to a much newer version of my source material at this point.
>> Everything from here on out will be in Python 3.11.

Dictionaries have methods that can be used to access the keys and values. Access either keys or values using the same keywords as methods. 
- dict_name.keys() / dict_name.values and you can list them too list(dict_name.keys())... you get it.
- the keys() and values() are methods used on the dictionaries.

Iterate over dictionaries using a for loop and an items() method. eg for item in dict_name.item(): ...


## Tuples
Similar to lists, but cannot be changed.
- tuples are immutable lists. Their values cannot be changed after initialization. 
- they are used to represent a fixed collection of items.
- a way to add to a tuple is to create a tuple of the items to append and then concatenate the existing tuple with the new one. eg fruits = ("apple", "banana"); fruits + ("watermelon", "orange").
- tuples also supoprt mixed types and nesting.


### Zipping
zipping is used to aggregate lists that have same index. Like pairing items with quantity but initially both are separate lists.
- the zip() method is used to accomplish this.
- after zipping, the resulting 'list' is a tuple. Use the list() method on it to turn it into a list.
- using the tuple() method on this, you can make it an explicit tuple
- throw in the dict() method and you can make it a dictionary.
- the zip() method can only be used once per iteration.


## Sets
Sets are an unordered collection of unique and immutable data objects. They operate on the principel of set mathematical theory.
- cannot be changed in place and no duplicate values.
- initialize sets by using the set() method on a list = set([data]) or putting the data in culy braces = {data}.
- items can be added to sets but these cannto be changed in place.

Set operations that can be used are: using set A and B
- union (|) - return a single set with all unique elements from Set A and Set B.
- intersection (&) - return a single set that contains only elements unique to Set A and Set B at the same time.
- difference (-) - return the difference between Set A and Set B
- issubset (<=) - used to check if a set is a subset of another
- issuperset (>=) - used to check if a set is the superset of another


## Parting Wisdom
- a list is used to store multiple objects and to retain a sequence, 
- a dictionary is used to store unique key-value pair mappings, 
- tuples are immutable, 
- and sets only store unique elements.

A couple of situations and what data structures to use:
1. definiing points in an x-y coordinate plane - use tuples. These points do not change.
2. numbering students in order - use lists. Because of order, list shines here
3. finding unique items from a bunch of items - use sets. Sets only take unique stuff
4. Organizing books and authors - use dictionaries. Dictionaries are good for storing attributes regarding items.

Choose the right data structure for efficiency and security sake. 