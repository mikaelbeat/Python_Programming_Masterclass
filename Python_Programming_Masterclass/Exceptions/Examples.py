
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    
try:    
    print(factorial(900))
except (RecursionError, ZeroDivisionError):
    print("\nThis program cannot calculate factorial number for such large number!")

print("\nProgram shutting down!")