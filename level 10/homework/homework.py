#task 2 priting numbers with intervals of 2

for number in range(1, 101, 2):
    print(number)

#task 3 printing numbers 1-1000 using while loop

number = 1

while number <= 1000:
    print(number)
    number = number + 1

#task 4 printing the sum of the numbers from 1-10

sum_numbers = 0
num = 1

while num <= 10:
    sum_numbers += num
    num += 1

print(sum_numbers)

#task 5 making examples of for loop and while loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(0, 10, 2):
    print(i)

num = 1
while num <= 5:
    print(num)
    num += 1

num = 2
while num <= 10:
    print(num)
    num += 2

total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(total)


product = 1
num = 1
while num <= 5:
    product *= num
    num += 1
print(product)

total = 0
num = 1
while total < 100:
    total += num
    num += 1
print(num)

for number in range(10, 0, -1):
    print(number)
