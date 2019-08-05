import shelve

with shelve.open("ShelfTest") as fruit:
    fruit["orange"] = "A sweet, orange citrus fruit"
    fruit["apple"] = "Good for making cider"
    fruit["lemon"] = "A sour, yellow citrus fruit"
    fruit["lime"] = "A sour, green citrus fruit"
    
    
print(fruit["lemon"])



# 5:21