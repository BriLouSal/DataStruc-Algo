def print_items(n: int):
    for i in range(n):
        for j in range(n):
            print(i, j)
        
      
        
# DO NOT CHANGE THIS LINE:
print_items(10)


# EXCPETED OUTPUT:
#  0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# Polynomial Time Complexity typically leads to a nested loop that is iterating through the variable n .