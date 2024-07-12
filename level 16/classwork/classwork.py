#task 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #0  #1 #2 #3 #4 #5 #6 #7 #8 #9 
print(list1)

#task 2
print(list1[:3])
print(list1[7:])
print(list1[3:7])

#task 3
print(list1[:-7])
print(list1[-3:])
print(list1[-7:-3])

#task 4
listn = [4, 2, 6, 7, 1, 12, 53, 42]

for i in listn:
    print(i)

#task 5

name = "vako"

for i in name:
    print(i)

#task 6

task6 = "vako sisauri cherry cream eggplant"


word1 = task6[0:4]   # vako
word2 = task6[5:12]  # sisauri
word3 = task6[13:19] # cherry
word4 = task6[20:23] # cream
word5 = task6[26:]   # eggplant

print("Word 1:", word1)
print("Word 2:", word2)
print("Word 3:", word3)
print("Word 4:", word4)
print("Word 5:", word5)