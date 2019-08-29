import random

class Enemy:
    
    def __init__(self, name="Enemy", hit_points=0, lives=0):
        self.name = name
        self._hit_points = hit_points
        self.lives = lives
        self._alive = True
        
    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >=0:
            self._hit_points = remaining_points
            print(f"I took {damage} points damage and have {self._hit_points} hit points left.\n")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"Enemy {self.name} lost a life!\n")
            else:
                print(f"Enemy {self.name} is dead!\n")
                self._alive = False
                      
    def __str__(self):
        return f"Name: {self.name}, Hit points: {self._hit_points}, Lives: {self.lives}.\n"
    
    
class Troll(Enemy):
    
    def __init__(self, name):
        super().__init__(name=name, hit_points=23, lives=1)
        
    def grunt(self):
        print(f"I {self.name}, will stomp you!\n")
        
        
class Vampyre(Enemy):
    
    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)
        
    def bite(self):
        print(f"I {self.name} will bite you!\n")
        
    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"***** {self.name} dodges *****\n")
            return True
        else:
            return False
        
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage = damage)
            
            
class VampyreKing(Vampyre):
    
    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140
        self._lives = 3
        
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage = (damage // 4))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        