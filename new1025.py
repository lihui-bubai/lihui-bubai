num = 123456
# using map
list_of_digits = list(map(int, str(num)))
print(list_of_digits)
# [1, 2, 3, 4, 5, 6]
# using list comprehension
list_of_digits = [int(x) for x in str(num)]
print(list_of_digits)
# [1, 2, 3, 4, 5, 6]

# finding frequency of each element in a list
from collections import Counter
my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) # defining a counter object
print(count) # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})
print(count['b']) # of individual element
