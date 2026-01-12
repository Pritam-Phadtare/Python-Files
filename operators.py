# Operators --- Operators are symbols or keywords used to perform operations on values and variables.
# Python has several operators for different task like arithmetic, comparison and more.

# Types of Operators ---
# 1. Arithmetic : Arithmetic operators are used to perform mathematical calculations / operations on 
# numbers.
# Types of Arithmetic operators ,

# | Operator | Name                   | Example           |
# | -------- | ---------------------- | ----------------- |
# | +        | Addition               | 10 + 3 = 13       |
# | -        | Subtraction            | 10 - 3 = 7        |
# | *        | Multiplication         | 10 * 3 = 30       |
# | /        | Division               | 10 / 3 = 3.333... |
# | %        | Modulus (remainder)    | 10 % 3 = 1        |
# | **       | Exponentiation (power) | 2 ** 3 = 8        |
# | //       | Floor division         | 10 // 3 = 3       |

# Examples ;
# a = 20
# b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# Python uses BODMAS rule which states anything inside brackets "(), [], {}" should be solved first and
# and multiplication and division should be done in precedence to addition and substraction.
# Example ;
# print(5 + 3 * 3 / 2)
# here , 3 / 2 --> 1.5 , 1.5 * 3 --> 4.5 , 5 + 4.5 --> 9

# print(4 - 2 * 4 / 2)
# here , 4 / 2 --> 2 , 2 * 2 --> 4 , 4 - 4 --> 0


# 2. Assignment : Assignment operators are used to assign value to a variable. Python also provide compound
# assignment opertors that perform operations like addition, substraction etc.

# | Operator | Example | Equivalent     |
# | -------- | ------- | -------------- |
# | =        | x = 5   | Assigns 5 to x |

# Example ;
# a = 20
# b = "Hello World"


# 3. Compound Assignment : Compund assignment operator combines arithmetic operations with assignment to
# a variable. We can say that it is a shortcut operator that combine an arithmetic operation with assignment.
# Types of Compund assignment operators ,

# | Operator | Example | Equivalent |
# | -------- | ------- | ---------- |
# | +=       | x += 3  | x = x + 3  |
# | -=       | x -= 3  | x = x - 3  |
# | *=       | x *= 3  | x = x * 3  |
# | /=       | x /= 3  | x = x / 3  |
# | //=      | x //= 3 | x = x // 3 |
# | %=       | x %= 3  | x = x % 3  |
# | **=      | x **= 3 | x = x ** 3 |

# Example ;

# Without compound assignemnt ,
# I am having an variable with value 5, we want to add 10 in it, then multiply it by 2, and flow divide it by
# 5.
# a = 5
# a = a + 10
# a = a * 2
# a = a // 5
# print(a)
# here, we need to add arithmetic operators and reassign value at each step which we can cutout using compund
# assignment operators.

# With compund assignment ,
# The same operations can be done with compound assignment operators where don't need to assign the arithmetic
# operators at each step.
# a = 5
# a += 10
# a *= 2
# a //= 5
# print(a)


# 4. Comparison : Comparison operator also called as relational operator are used to compare two values.
# The comparison operator always provide boolean result "true or false".
# Types of comparison operators ,

# | Operator | Name                  | Example               |
# | -------- | --------------------- | --------------------- |
# | ==       | Equal to              | 10 == 10 returns True |
# | !=       | Not equal to          | 10 != 5 returns True  |
# | >        | Greater than          | 10 > 5 returns True   |
# | <        | Less than             | 10 < 5 returns False  |
# | >=       | Greater than or equal | 10 >= 10 returns True |
# | <=       | Less than or equal    | 5 <= 10 returns True  |

# Examples ;
# a = 10
# b = 20
# print(a == b)
# print (a != b)
# print (a > b)
# print (a < b)
# print (a >= b)
# print (a <= b)