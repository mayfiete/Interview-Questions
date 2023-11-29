'''
What is the difference between list and tuples in Python?
Lists are mutable, meaning their elements can be changed, while tuples are immutable, meaning their elements cannot be changed after creation
'''

'''
Question: Write a Python function to sum all the numbers in a list.
Example Input: [1, 2, 3, 4, 5]
Expected Output: 15
'''

'''
What is inheritance?
'''

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