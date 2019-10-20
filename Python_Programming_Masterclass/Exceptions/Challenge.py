

def calculator():
    number1 = int(input("\nEnter first number: "))
    number2 = int(input("\nEnter second number: "))
    sum = number1 // number2
    return f"\nValue {number1} divided by {number2} is {sum}."

try:
    print(calculator())
except ValueError:
    print("\nPlease enter only integer values!")
    print("\nTry again!")
    print(calculator())
finally:
    print("\nEnding program!")