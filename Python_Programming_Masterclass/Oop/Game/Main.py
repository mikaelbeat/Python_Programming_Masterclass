import Player, Enemy

print("\n*************** Player ***************\n")

mikaelbeat = Player.Player("Mikaelbeat")
 
mikaelbeat.lives -= 2
print(mikaelbeat)
 
mikaelbeat.lives += 5
mikaelbeat.level += 3
print(mikaelbeat)


print("\n*************** Basic enemy ***************\n")
 
monster = Enemy.Enemy("Basic enemy", 12, 1)
print(monster)
 
monster.take_damage(5)
print(monster)
 
 
print("\n*************** Troll ***************\n")
 
ugly_troll = Enemy.Troll("Ugly troll")
print(ugly_troll)
ugly_troll.grunt()
ugly_troll.take_damage(10)
 
cave_troll = Enemy.Troll("Cave troll")
print(cave_troll)
cave_troll.grunt()
cave_troll.take_damage(15)
 
 
print("\n*************** Vampyre ***************\n")
 
dracula = Enemy.Vampyre("Dracula")
print(dracula)
dracula.bite()
dracula.take_damage(5)
 
# while dracula._alive:
#     dracula.take_damage(1)
#     print(dracula)
    
    
print("\n*************** Vampyre King***************\n")

vlad = Enemy.VampyreKing("Vlad")
print(vlad)
vlad.take_damage(50)
print(vlad)








