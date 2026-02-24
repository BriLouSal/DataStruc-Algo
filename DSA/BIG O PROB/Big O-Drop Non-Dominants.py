

def print_items(n: int):
    for i in range(n):
        for j in range(n):
            print(i, j)
            
    for k in range(n):
        print(k)
            
            # We'd get O(n^2 + n) but we drop the non-dominant term and we get O(n^2) so we drop O(n^2)
# DO NOT CHANGE THIS LINE:
print_items(10)


# Another example
def items(n: int):
    for i in range(n):
        print(i)
    for j in range(n):
        for k in range(n):
            print(j, k)
            
            # We'd get O(n^2 + n) but we drop the non-dominant term and we get O(n^2) so we drop O(n^2), because we're actually looking at where the Big O grows much more significantly as n increases, so we drop the O(n) and we get O(n^2)
            
# Side: O(1)


def addition(n: int):
    return n + n

    