class Wing(object):
    
    def __init__(self, ratio):
        self.ratio = ratio
        
    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun!!!")   
        elif self.ratio == 1:
            print("This is hard work, but I am flying")
        else:
            print("I think I'll just walk")
    

class Duck(object):
    
    def __init__(self):
        self._wing = Wing(1.8)
    
    def walk(self):
        print("Waddle, waddle, waddle")
        
    def swim(self):
        print("Come on it, the water is lovely")
        
    def quack(self):
        print("Quack, quack")
        
    def fly(self):
        self._wing.fly()
        
        
class Penquin(object):
    
    def walk(self):
        print("Waddle, waddle, I waddle too")
        
    def swim(self):
        print("Water is very chilly here")
        
    def quack(self):
        print("Penquins don't quack")
        
        
def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()
   
    
if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)
    donald.fly()
    
    
    print("\n**********\n")
    
    
    percy = Penquin()
    test_duck(percy)
    
    
    
    
    
    
    