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


cave_troll = Enemy.Troll("Cave troll")
print(cave_troll)
cave_troll.grunt()