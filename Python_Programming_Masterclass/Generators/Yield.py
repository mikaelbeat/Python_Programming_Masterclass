

def calculator(value):
    yield value + 1
    yield value + 2
    yield value + 3
    
    
value = calculator(10)

for x in value:
    print(x)