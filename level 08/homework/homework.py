#task 2 - testing operations - !=, <= and >=
print(10 != 50)
print(10 <= 50)
print(10 >= 50)

#task 3 - testing operations (==, !=, >=, <=, >, <, and, or.) with variables.

num1 = 15
num2 = 179
num3 = 1
num4 = 2
num5 = 50
num6 = 28
num7 = 17
num8 = 23 == 23 #True
num9 = 17 > 5 #True
num10 = 17 < 5 #False
num11 = 32 != 50 #True
num12 = 40 >= 39 #True
num13 = 40 <= 39 #False

print(num1 > num2) #False
print(num2 > num1) #True
print(num1 > num4) #True
print(num5 > num2) #False
print(num4 < num6) #True
print(num7 < num3) #False
print(num1 == num3) #False
print(num2 != num6) #True
print(num7 <= num5) #True
print(num5 >= num1) #True
print(num10 and num9) #False
print(num10 and num8) #False
print(num8 and num9) #True
print(num8 or num9) #True
print(num9 or num10) #True
print(num13 and num9) #False
print(num12 or num11) #True
print(num13 and num8) #False
print(num12 and num9) #True
print(num12 and num11) #True
print(num12 or num8) #True


#task 4
    # the difference between "and" and "or" operations.
    # the "and" operation operation returns True only if both conditions on its left and right sides are True. If either condition is False, the result is False. It's like saying, "Is this true AND that true?" If both are true, then the whole thing is true. Otherwise, it's false
    # the "or" This operation returns True if at least one of the conditions on its left or right sides is True. It's like saying, "Is this true OR that true?" If either one is true, then the whole thing is true.


#task 5

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print(num2 > num1)
print(num2 < num1)
print(num2 == num1)