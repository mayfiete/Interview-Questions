'''
What is the difference between list and tuples in Python?
'''

'''
Question: Write a Python function to sum all the numbers in a list.
Example Input: [1, 2, 3, 4, 5]
Expected Output: 15
'''

'''
What is inheritance?
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Hello')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Woof')

'''
What is a decorator?
When would you use one?
'''

'''
What's the difference between a class and a function?
Give me an example of when you would use each.
'''

def count_to_ten():
    for i in range(1,11):
        print(i)


class CountToTen:
    def __init__(self):
        self.numbers = [1,2,3,4,5,6,7,8,9,10]

    def count(self):
        for i in self.numbers:
            print(i)


'''
When might you use list comprehensions?
'''


# What is a list comprehension and provide an example.

# Answer: A list comprehension provides a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. Example: [x**2 for x in range(10)] creates a list of squares for numbers 0 to 9.
# Explain the difference between a tuple and a list.

# Answer: Both tuples and lists are used to store collections of items. The main difference is that tuples are immutable (cannot be modified after creation) while lists are mutable. Tuples are defined using parentheses (e.g., (1, 2, 3)) and lists with square brackets (e.g., [1, 2, 3]).
# How does a Python function differ from a Python method?

# Answer: A Python function is a block of code that performs a specific task and is defined using the def keyword. A method in Python is similar to a function but is associated with an object (defined within a class). It can access and modify the state of the object.
# What is a lambda function in Python?

# Answer: A lambda function is a small anonymous function defined with the lambda keyword. It can take any number of arguments but can only have one expression. Example: lambda x: x * 2 doubles the input value.
# What is the purpose of the self keyword in Python classes?

# Answer: self refers to the instance of the class. It is used to access variables and methods that belong to the class. It's a conventional way to refer to the instance within class methods.
# How do you handle exceptions in Python?

# Answer: Exceptions in Python are handled using the try-except block. The code that might raise an exception is placed in the try block, and the handling of the exception is done in the except block. There's also an optional finally block.
# What does the __init__ method do in Python?

# Answer: The __init__ method is a special method in Python classes. It's called when an object is created from a class and allows the class to initialize the attributes of the class.
# What are decorators in Python?

# Answer: Decorators in Python are a powerful tool that allows modification of the behavior of a function or a class. A decorator is a function that takes another function as an argument, adds some functionality, and returns another function, without altering the source code of the original function.
# Explain the difference between break, continue, and pass.

# Answer: In Python, break exits the closest enclosing loop, continue skips the rest of the current loop iteration and moves to the next iteration, and pass is a null statement that does nothing and is used as a placeholder.