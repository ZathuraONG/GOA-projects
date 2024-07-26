#task 2 - create 2 int type variables and output the sum

num1 = 10
num2 = 5

print(num1 + num2)

#task 3 - create 2 str type variable and output to the screen

str1 = "vako"
str2 = "sisauri"

print(str1 + str2) #this is called concatenation and happens when we try adding two strings

#task 4 create 2 int type variables divide them and explain why it resulted in a float and not an integer

print(num1 / num2) #this results in a float because the program doesnt know beforehand if the result will be a full number or not, it is an implicit conversion, meaning it happens automatically without requiring explicit instruction from the programmer.

#task 5 rehearsing comperative operations

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)


#task 6 mixing up the operations

print(12 + 8 == 16 + 4) #True
print(5 / 2 < 5 / 1) #True
print(4 * 5 > 6 * 7) #False
print(14 - 7 == 4) #False

#task 7 all logical operations

print(True and True)  #True
print(True and False)  #False
print(True or False)  #True
print(False or False)  #False
print(not True)  #False
print(not False)  #True
print(True != False)  #True
print(True != True)  #False

#task 8 mixing comperative operations with logical operations 

print(14 > 3 and False) #False
print(23 < 15 or False) #False
print(8 == 3 and False) #False
print(52 <= 54 or True) #True
print(15 != 4 and True) #True


#task 9 making for loop print numbers 1-10


for i in range(1, 10):
    print(i)


#task 10 printing the sum of the numbers from a list 

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0

for i in list1:
    sum += i

print(sum)

#task 11 printing every letter of a string one by one using for loop

str1 = "Hello, World!"

for i in str1:
    print(i)

#task 12 printing numbers 1-10 using while loop

num1 = 1

while num1 < 10:
    print(num1)
    num1 = num1 + 1

#task 13 printing numbers 1-100 but skipping 50-60

num1 = 1

while num1 < 100:
    if num1 < 50 or num1 > 60:
        print(num1)
    num1 = num1 + 1

#task 14 adding numbers until it reaches 50

sum = 0
num1 = 1

while sum < 50:
    sum += num1
    num1 += 1
    print(sum)

#task 15 function to check divisibility


def check_divisibility():
    number = int(input("Enter a number: "))
    
    if number % 3 == 0 or number % 5 == 0:
        print(f"The number {number} is divisible by 3 or 5 or both.")
    else:
        print(f"The number {number} is not divisible by 3 or 5.")

check_divisibility()

#task 16 finding the arithmetical middle index of the list 


def find_middle(numbers):
    sorted_numbers = sorted(numbers)
    
    middle_index = len(sorted_numbers) // 2
    
    return sorted_numbers[middle_index]

#Test
list1 = [1, 2, 5, 4, 3]
middle_number = find_middle(list1)
print(middle_number)

#task 17 


def every_second_uppercase(s):
    result = ''.join(
        char.upper() if (i % 2 != 0) else char
        for i, char in enumerate(s)
    )
    return result


#Test
str1 = "hello world"
new_string = every_second_uppercase(str1)
print(new_string)



#task 18

list1 = [1, 2, 3, 4, 5]

def square_numbers(numbers):

    squared_list = []
    
    for i in numbers:
        squared_list.append(i ** 2)
    
    return squared_list

#Test
squared = square_numbers(list1)
print(squared)