

# write function to count to ten 
def count_to_ten():
    for i in range(1,11):
        print(i)

count_to_ten()

# write function to add values in a list

list = [1,2,3,4,5]
def add_list_values(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(add_list_values(list))