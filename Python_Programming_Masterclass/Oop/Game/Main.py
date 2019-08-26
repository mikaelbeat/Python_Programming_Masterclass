import Player

mikaelbeat = Player.Player("Mikaelbeat")

print(mikaelbeat.name)
print(mikaelbeat.lives)

mikaelbeat.lives -= 2
print(mikaelbeat.lives)



print(mikaelbeat)

mikaelbeat.lives -= 50
print(mikaelbeat)

print("\n*************** Challenge ***************\n")

mikaelbeat.level += 3
print(mikaelbeat)

mikaelbeat.level -= 1
print(mikaelbeat)

mikaelbeat.score = 4500
print(mikaelbeat)