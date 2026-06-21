
# Speeds up standard input and output operations
import sys


input = lambda: sys.stdin.readline().rstrip("\r\n")
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)

def solve():
    # Write your main logic here
    pass

if __name__ == "__main__":
    solve()

# Increases standard recursion depth to prevent runtime errors
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().rstrip("\r\n")
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)

def solve():
    # Write your main logic here
    
    # You input by how much snow has fallen and you need to find out how many days it will take for the snow to melt
    ask = int(input())
    for i in range(ask):
        snow = int(input())
        days = 0
        while snow > 0:
            days += 1
            snow -= days
        print(days)
if __name__ == "__main__":
    # Handles problems with multiple test cases (e.g., Codeforces Div. 2/Div. 3)
    t = int(input())
    for _ in range(t):
        solve()