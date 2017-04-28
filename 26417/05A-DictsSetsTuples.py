# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:52:05 2017
@filename: 03A-ListsDictsSetsTupples
@author: cyruslentin
"""

# Containers
# Python includes several built-in container types: dictionaries, sets,
# and tuples.

# Dictionaries
# A dictionary stores (key, value) pairs, similar to a Map in Java or an 
# object in Javascript. 
# You can use it like this:
d = {'cat': 'cute', 'dog': 'furry'} # Create a new dictionary with some data
print(d['cat'])                     # Get an entry from a dictionary; prints "cute"
print('cat' in d)                   # Check if a dictionary has a given key; prints "True"
print('cute' in d)
d['fish'] = 'wet'                   # Set an entry in a dictionary
print(d['fish'])                    # Prints "wet"
#print(d['monkey'])                  # KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))       # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))         # Get an element with a default; prints "wet"
del d['fish']                       # Remove an element from a dictionary
print(d.get('fish', 'N/A'))         # "fish" is no longer a key; prints "N/A"

# Loops: 
# It is easy to iterate over the keys in a dictionary:
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"

# If you want access to keys and their corresponding values, use the 
# iteritems method:
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"

# Dictionary comprehensions: 
# These are similar to list comprehensions, but allow you to easily construct 
# dictionaries. 
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"

# Sets
# A set is an unordered collection of distinct elements. As a simple example, 
# consider the following:
animals = {'cat', 'dog'}
print('cat' in animals)             # Check if an element is in a set; prints "True"
print('fish' in animals)            # prints "False"
animals.add('fish')                 # Add an element to a set
print('fish' in animals)            # Prints "True"
print(len(animals))                 # Number of elements in a set; prints "3"
animals.add('cat')                  # Adding an element that is already in the set does nothing
print(len(animals))                 # Prints "3"
animals.remove('cat')               # Remove an element from a set
print(len(animals))                 # Prints "2"

# Loops: 
# Iterating over a set has the same syntax as iterating over a list; 
# however since sets are unordered, you cannot make assumptions about the 
# order in which you visit the elements of the set:
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    #print('#%d: %s' % (idx + 1, animal))
    print('#{}: {}'.format(idx + 1, animal))
# Prints "#1: fish", "#2: dog", "#3: cat"

# Set comprehensions: 
# Like lists and dictionaries, we can easily construct sets using set 
# comprehensions:
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)  # Prints "set([0, 1, 2, 3, 4, 5])"

# Tuples
# A tuple is an (immutable) ordered list of values. 
# A tuple is in many ways similar to a list; one of the most important 
# differences is that tuples can be used as keys in dictionaries and 
# as elements of sets, while lists cannot. 
d = {(x, x + 1): x for x in range(10)}      # Create a dictionary with tuple keys
print(d)
t = (5, 6)                          # Create a tuple
print(t)
print(type(t))                      # Prints "<type 'tuple'>"
print(d[t])                         # Prints "5"
print(d[(1, 2)])                    # Prints "1"
