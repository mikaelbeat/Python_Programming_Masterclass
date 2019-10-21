import Ducks

flock = Ducks.Flock()
donald = Ducks.Duck()
daisy = Ducks.Duck()
duck3 = Ducks.Duck()
duck4 = Ducks.Duck()
duck5 = Ducks.Duck()
duck6 = Ducks.Duck()
duck7 = Ducks.Duck()
percy = Ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)
flock.add_duck(percy)

flock.migrate()