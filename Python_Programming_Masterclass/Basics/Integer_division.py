
# // -> Floor division - division that results into whole number


bun_price = 2.40

money = 15

 
if money > bun_price:
    buns = money // bun_price
    amount = round(bun_price * buns, 2)
    money_left = round(money - amount, 2)
 
print(f"You can afford to {buns} buns for the cost {amount}.")
print(f"Total money was {money} and you get {money_left} back.")

