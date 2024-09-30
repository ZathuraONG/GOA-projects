#1
tuples_list = [(1, 'banana'), (2, 'apple'), (3, 'orange')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])


#2
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))


#3
words = ['apple', 'banana', 'pear', 'kiwi', 'date']
filtered_words = list(filter(lambda x: len(x) == 4, words))


#4
strings = ['hello', 'world', 'python']
uppercase_strings = list(map(lambda x: x.upper(), strings))


#5
number_list = [1, 2, 3, 4, 5]
multiplied_numbers = list(map(lambda x: x * 5, number_list))


#6
words = ['apple', 'banana', 'cherry']
connected_words = list(map(lambda x: x[0] + '-start', words))


#7
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))


#8
words = ['apple', 'banana', 'Avocado', 'kiwi', 'Apricot']
a_words = list(filter(lambda x: x.lower().startswith('a'), words))


#9
remaining_numbers = list(filter(lambda x: x % 2 != 0, numbers))

