#task 1

def mean(listn):
    return sum(listn) / len(listn)

print(mean([1,2,3,4]))

#task 2

def manual_abs(num):
    if num >= 0:
        return num
    else:
        return -num
    
print(manual_abs(-8))


#task 3

def remove_duplicates(listn):
    return list(set(listn))

print(remove_duplicates([1,1,2,2,4,5,6,7,7]))

#task 4 codewars
