#task 1 
# We create a dictionary opposite that holds pairs of opposite directions, then we use a list called result to store the simplified directions and then iterate through each direction in the input list using for loop If the last direction in the result list is the opposite of the current direction, we remove the last direction from the result list. otherwise, we add the current direction to the result list.

#task 4
#1
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 5, numbers))

#2
string_numbers = ["1", "2", "3", "4", "5"]
result = list(map(int, string_numbers))

#3
words = ["hello", "world", "python"]
result = list(map(lambda x: x + "!", words))

#4
import math
numbers = [1, 4, 9, 16, 25]
result = list(map(math.sqrt, numbers))

#5
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x % 2 == 0, numbers))