#task 1

age = int(input("Please enter your age:"))

if age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teen")
else:
    print("You are a grownup")

#task 2

i = 1

while i <= 100:
   
    if 40 <= i <= 50:
        pass
    else:
        print(i)
    
    i = i + 1