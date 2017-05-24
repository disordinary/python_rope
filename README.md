# python_rope
A Rope is a datastructure to store a very long string in a binary tree made up of multiple smaller strings. Because you're working with small(ish) strings it is generally more efficient for most opperations. 

https://en.wikipedia.org/wiki/Rope_(data_structure)

## Usage
The rope constructor contains requires a string, it also has the optional `optimalLength`, `minLength`, and `maxLength` arguments.

The `optimalLength` argument is the length that we consider optimal for a string, it defaults to 1000 but that is an arbitrary number and is not backed by any benchmarking.
The `minLength` argument is the minumum length that a leaf can be before it triggers a re-balance, once again it is a number that has been plucked from the air and defualts to 500.
The `maxLength` argument is the maximum length that a leaf node can be before it triggers a re-balance, as with the `minLength` it is an arbitrary number set at 1500.

```Python
from rope import Rope
bigString = Rope(aVeryLongString)
```

The Rope itself has `insert` and `delete` methods.

`Insert` takes an offset within the long string and a string to insert.

```Python
bigString.insert(3000, "FOO")
```

`Delete` takes an offset within the long string and a lenght to delete.

```Python
bigString.delete(3000, 3)
```

To convert back to a string:
```Python
print str(bigString)
```
