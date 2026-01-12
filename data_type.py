# Data Type --- Data type is a concept or a classification through which we can assign different types
# or kind of values to a variable, it can be number, charachters, and many more. As variable holds a
# value and that value determines the type of data type the variable is using.
# Python has built-in data-types for different kinds of data.

# Comman Data Types ---
# 1. Numeric : int(whole numbers 0-9), float(decimal numbers), complex(imaginery number).
# 2. Text : str(strings like "hello").
# 3. Collections : list, tuple, dict, set (used to store multiple values in different ways).
# 4. Boolean : bool (True of False).
# 5. None : NoneType (represents no value using none).


# 1. Numeric ---

# a. integer (int) : int is data type by which you proivde the whole numbers as an value to a variable.
# Example ;
# abc = 20
# print(type(abc))

# b. float : floats is a data type by which you can provide the decimal numbers and fraction value to a
# variable.
# Example ;
# abc = 12.5
# print(type(abc))
# xyz = 12/3
# print(type(abc))

# c. complex : complex is a data type by which we can provide real and imaginery numbers to a variable.
# Example ;
# abc = 123j
# print(type(abc))


# 2. Text ---
# String (str) : string is a data type by which you can store or provide alphanumeric value to a variable.
# Example ;
# abc = "pritam@123"
# print(type(abc))


# 3. Boolean ---
# bool : Theres nothing much to say this is the data type which will and always give the result of True and
# False.
# Example ;
# abc = True
# print(type(abc))


# 4. None --- represents no value to the variable.
# Example ;
# abc = None
# print(type(abc))

# The collections data type will be covered later.

# -------------------------------------------------------------------------------------------------------------

# String Indexing --- String indexing is the way to access individual characters in a string using their position
# (index) with square brackets[]. Python uses zero-based indexing meaning the first character is at index 0.
# - Positive Indexing starts from the beginning 0, 1, 2, an so on.
# - Negative indexing starts from the end of the string -1 is the last character, -2 is the second last and so on.
# Example ;
# abc = "Pritam Phadtare"
# print(abc[2])


# String Slicing --- String slicing is a way by which you can take a part of a string also be named as substring by
# specifying a range of character positions using indexes inside the square brackets.
# It uses general form abc[start:end:step]
# where, start is inclusive, end is exclusive, and step controls how many characters to skip.
# abc = "Pritam Phadtare"
# print(abc[1:10])

# ---------------------------------------------------------------------------------------------------------------

# Type Conversion --- Type conversion is a process of changing a value of one data type to another. For example 
# converting the string "10" to integer 10, or the integer 5 to float 5.0

# Types of type conversion in python :
# 1. Implicit : In implicit conversion python automatically converts the value to another data type, commonly when
# mixing int and float.
# 2. Explicit : In explicit we users manually convert the data type using in built functions like str(), int(), float(),
# complex(), list(), set(), bool().

# Examples ;
# 1. Implicit :
# a = "20"
# b = int(a)
# print(type(b))

# a = 20
# b = str(a)
# print(type(b))

# a = 12
# b = float(a)
# print(b)