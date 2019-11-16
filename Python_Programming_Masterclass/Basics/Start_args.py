

def sum_all_numbers(*args):
    sum = 0
    numbers = []
    for value in args:
        sum += value
        numbers.append(value)
    print(f"Sum of all values {numbers} is {sum}.")
    
    
sum_all_numbers(5, 6, 3, 1)