




# Question 1:Binary Search in Sorted Array
##Given a sorted array and a target value, determine if the value exists.
#Hint: Repeatedly halve the search space.

# arr = [1,3,5,7,9,11]
# target = 7


# Index = 3



# This would be a LogO(n) because we're iterating through the data of n which is our array and we're looking if it exists.
def find_target(target: int, arr: list) -> int:
    for index, value in enumerate(arr):
        if value == target:
            return f" Index = {index}"


    return None




output = find_target(target= 7, arr=[1,3,5,7,9,11])

print(output)