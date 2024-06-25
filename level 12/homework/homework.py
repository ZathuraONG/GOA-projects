#task 2 - dice roll game

#the correct answer
correct_answer = 4

#User guess
user_guess = int(input("Enter your guess (1 to 6): "))

# Check if the guess is correct
if user_guess == correct_answer:
    print("It's correct!")
else:
    print(f"It's incorrect. The correct answer was {correct_answer}.")


#task 3 - Using for loop to output the sum of the numbers from 1 to 100

sum_numbers = 0

for i in range(1, 101):
    sum_numbers += i

print(sum_numbers)


#task 4 - 4) Using for loop to output the sum of the numbers from 1 to 1000 but wihout the numbers in the range(500, 600)

sum_numbers = 0

for i in range(1, 1001):
    if 500 <= i < 600:
        pass
    else:
        sum_numbers += i

print(sum_numbers)


#task 5 5) Using while loop to make a game similar to the second task but keep asking for the correct answer until they guess it successfully

correct_number = 7 
user_guess = 0

while user_guess != correct_number:
    user_guess = int(input("Enter your guess (1 to 10): "))
    if user_guess == correct_number:
        print("It's correct!")
    else:
        print("It's incorrect. Try again.")

#task 6 Using while loop to output the product of numbers from 1 to 10

product = 1
num = 1

while num <= 10:
    product = product * num  # Augmented assignment operator
    num += 1

#task 7 make the user input a number and tell if it is odd or even

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#task 8 Grading system

score = int(input("Enter your score: "))


if 90 <= score <= 100:
    grade = "Grade A"
elif 80 <= score < 90:
    grade = "Grade B"
elif 70 <= score < 80:
    grade = "Grade C"
elif 60 <= score < 70:
    grade = "Grade D"
elif 0 <= score < 60:
    grade = "Grade F"
else:
    grade = "Invalid score. Please enter a score between 0 and 100."

print(f"Your grade is: {grade}")