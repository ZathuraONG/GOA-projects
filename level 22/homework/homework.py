#task 2
def manual_min(num):
    
    min_number = num[0]
    for i in num:
        if i < min_number:
            min_number = i
    return min_number

print(manual_min([5,4,6,7,8]))

#task 3

def manual_max(num):
    
    max_number = num[0]
    for i in num:
        if i > max_number:
            max_number = i
    return max_number

print(manual_min([5,4,6,7,8]))


#task 4

def manual_len(listn):
    count = 0
    for i in listn:
        count = count + 1
    return count

print(manual_len([2,4,5,1,6,2,5,6]))

#task 5

def manual_sum(listn):
    total = 0
    for i in listn:
        total = total + i
    return total

print(manual_sum([5,5,2,5,1,7]))

#task 6
def manual_replace(listn, old_value, new_value):
    result = []
    for i in listn:
        if i == old_value:
            result.append(new_value)
        else:
            result.append(i)
    return result

print(manual_replace([1,2,3,4,5], 4, 6))

#task 7

def manual_find(listn, value):
    for index, i in enumerate(listn):
        if i == value:
            return index
        
print(manual_find([1,2,3,4,5,6,7,8], 4))
