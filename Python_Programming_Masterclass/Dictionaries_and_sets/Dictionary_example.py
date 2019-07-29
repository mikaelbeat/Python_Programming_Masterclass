
fruit = {"orange": "A sweet, orange citrus fruit",
         "lemon": "A sour, yellow citrus fruit"}

while True:
    search = input("Please enter a fruit: ")
    if search == "quit":
        break
    if search in fruit:
        search_result = fruit.get(search)
        print(search_result)
    else:
        print(f"Sorry, we don't have {search}.")