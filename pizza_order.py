print("Welcome to Python Pizza Deliveries!")
print("Small pizza is $15\nMedium pizza is $20\nLarge pizza is $25\nfor small pizza Pepperoni is $2\nfor medium / large pepperoni is $3\nextra cheese is $1")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill = bill + 2

elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill = bill + 3
else:
    bill = 25
    if pepperoni == "Y":
        bill = bill + 3

if pepperoni=="N":
        bill = bill
if extra_cheese == "Y":
        bill = bill + 1
if extra_cheese=="N":
        bill = bill
print(f"your total bill is ${bill}")