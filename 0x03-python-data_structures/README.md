This directory has been used for all projects related to data structures in Python, specifically Lists and Tuples.

A. listsin Python
what are they?

Lists are ordered collections of items in Python. They can hold various data types like integers, strings, floats, booleans, and even other lists! This flexibility makes them a powerful tool for storing and managing diverse data.

Key characteristics:

Mutability: Elements in a list can be changed after creation (mutable).
Ordering: Items are maintained in the order they are added.
Accessing elements: You can access elements using numerical indexes starting from 0.
How to use them:

Creating Lists:

Use square brackets [] to enclose the elements separated by commas.

Accessing Elements:

Use the index (position) within square brackets after the list name.

Modifying Lists:

Use indexing to change existing elements or assign new values.
Common List Methods:

Python offers various methods for manipulating lists. Here are a few examples:
append(x): Adds an element x to the end of the list.
insert(i, x): Inserts an element x at a specific index i.
remove(x): Removes the first occurrence of element x from the list.
pop(i): Removes and returns the element at index i (defaults to the last element if no index provided).
sort(): Sorts the list elements in ascending order.
reverse(): Reverses the order of elements in the list.

***************
Tuples in Python
What are they?

Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation. They offer a way to store ordered collections where data integrity is essential.

Key characteristics:

Immutability: Elements in a tuple cannot be modified after creation.
Ordering: Similar to lists, items are maintained in the order they are added.
Accessing elements: Use indexing similar to lists.
How to use them:

Creating Tuples:

Use parentheses () to enclose the elements separated by commas.

Accessing Elements:

Use indexing the same way as with lists.
Important Note: Since tuples are immutable, methods like append(), insert(), and remove() wouldn't work as they attempt to modify the tuple.

When to use tuples:

Use tuples when you need a fixed collection of data that shouldn't be altered after creation.
Tuples are useful for representing data structures like coordinates or representing configuration values.
They are also used as dictionary keys because dictionaries require immutable keys for efficient lookups.
