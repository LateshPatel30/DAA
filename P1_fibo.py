# =====================================================
# Program: Fibonacci Numbers using Recursive and Iterative Methods
# =====================================================

def rec(n):
    """Recursive Fibonacci"""
    if n == 0 or n == 1:
        return n
    else:
        return rec(n - 1) + rec(n - 2)

def rrr(n):
    """Iterative Fibonacci"""
    if n <= 0:
        print("Enter a positive integer")
    elif n == 1:
        print(0)
    else:
        a, b = 0, 1
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c
        print()

n = int(input("Enter the number of terms: "))

print("\n=== Fibonacci using Recursive Method ===")
for i in range(n):
    print(rec(i), end=" ")
print("\n")

print("=== Fibonacci using Iterative Method ===")
rrr(n)

# Recursive Time Complexity  : O(2^n)
# Recursive Space Complexity : O(n) (due to recursion stack)
# Non-Recursive Time Complexity : O(n)
# Non-Recursive Space Complexity: O(1) (uses constant memory)