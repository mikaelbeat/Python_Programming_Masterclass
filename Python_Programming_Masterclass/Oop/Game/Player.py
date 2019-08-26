

class Player(object):
    
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
        
    def get_name(self):
        return self.name
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative!")
            self._lives = 0
        
    def _get_lives(self):
        return self._lives
    
    lives = property(_get_lives, _set_lives)
    
    def __str__(self):
        return f"Name: {self.name}, Lives: {self._lives}, Level: {self._level}, Score: {self._score}"
    
    
    
    def _set_level(self, level):
        if level >= 1:
            score_multiplier = level - self._level
            temp_score = score_multiplier * 1000
            if temp_score >= 0:
                self._score = temp_score
            else:
                self._score = 0
            self._level = level
        else:
            print("Level cannot go below one!")
            self._level = 1
            
    def _get_level(self):
        return self._level
    
    level = property(_get_level, _set_level)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
    
            
        