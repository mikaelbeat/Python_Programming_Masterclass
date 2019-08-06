class Kettle(object):
    
    power_source = "Electricity"
    
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
        
    def switch_on(self):
        self.on = True
        return "Kettle is turned on!"
        
        
kenwood = Kettle("Kenwood", 8.99)
print(f"Price for Kenwood is {kenwood.price}.")
print(kenwood.switch_on())
print(f"Kenwood power source is {kenwood.power_source}.")

print("\n****************************\n")

hamilton = Kettle("Hamilton", 12.00)
print(f"Price for Hamilton is {hamilton.price}.")
hamilton.power_source = "Atomic"
print(f"Hamilton power source is {hamilton.power_source}.")