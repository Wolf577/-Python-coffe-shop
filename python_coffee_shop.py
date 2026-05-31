print("hello welcome to the coffee shop!!!!!!!")

itemsavailabe = (
    "latte - 10\n"
    "latte (with whipped cream) - 15\n"
    "decaf  - 5\n"
    "cappucino  - 8\n"
    "espresso  - 9\n"
)

name = input("What is your name good sir/mam?\n")

if name == "John" or name == "john":
    evil_status = input(
        "excuse me dear sir/mam but may i know if you are evil john\n"
    )

    if evil_status == "yes" or evil_status == "Yes":
        print("sorry good sir/mam but you are not welcome here")
        exit()

    else:
        print("sorry for the inconvenience sir/mam please have some coffee")

order = input(
    "What will be your order for today mister/mistress "
    + name
    + " todays special are \n"
    + itemsavailabe
    + "\n"
)

if order == "latte" or order == "Latte":
    price = 10
    recommandation = input("do you wish to have some whipped cream in it too my dear sir/mam \n")

    if recommandation == "yes" or recommandation == "Yes":
        price = 15
    else:
        price = 10


elif order == "decaf" or order == "Decaf":
    price = 5

elif order == "cappucino" or order == "Cappucino":
    price = 8

elif order == "espresso" or order == "Espresso":
    price = 9

else:
    print("Sorry we don't have that item")
    exit()

quantity = input("How many " + order + "'s would you like to order?\n")

total = price * int(quantity)

print("sure that will cost you $" + str(total))

print(
    "thank you for coming to the coffee shop your "
    + quantity
    + " "
    + order
    + "'s is coming right up please wait for a while"
)