CASH_ON_HAND = 550
WATER_ON_HAND = 400
MILK_ON_HAND = 540
BEANS_ON_HAND = 120
CUPS_ON_HAND = 9

print("The coffee machine has:")
print("{} of water".format(WATER_ON_HAND))
print("{} of milk".format(MILK_ON_HAND))
print("{} of coffee beans".format(BEANS_ON_HAND))
print("{} of disposable cups".format(CUPS_ON_HAND))
print("{} of money".format(CASH_ON_HAND))

print("\nWrite action (buy, fill, take): ")
choice = input()
if choice.lower() == "buy":
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    drink_option = int(input())
    if drink_option == 1:
        WATER_ON_HAND -= 250
        BEANS_ON_HAND -= 16
        CUPS_ON_HAND -= 1
        CASH_ON_HAND += 4
    elif drink_option == 2:
        WATER_ON_HAND -= 350
        MILK_ON_HAND -= 75
        BEANS_ON_HAND -= 20
        CUPS_ON_HAND -= 1
        CASH_ON_HAND += 7
    elif drink_option == 3:
        WATER_ON_HAND -= 200
        MILK_ON_HAND -= 100
        BEANS_ON_HAND -= 12
        CUPS_ON_HAND -= 1
        CASH_ON_HAND += 6

    print("The coffee machine has:")
    print("{} of water".format(WATER_ON_HAND))
    print("{} of milk".format(MILK_ON_HAND))
    print("{} of coffee beans".format(BEANS_ON_HAND))
    print("{} of disposable cups".format(CUPS_ON_HAND))
    print("{} of money".format(CASH_ON_HAND))

elif choice.lower() == "fill":
    print("Write how many ml of water do you want to add: ")
    fill_water = int(input())
    print("Write how many ml of milk do you want to add: ")
    fill_milk = int(input())
    print("Write how many grams of coffee beans do you want to add: ")
    fill_beans = int(input())
    print("Write how many disposable cups of coffee do you want to add: ")
    fill_cups = int(input())

    WATER_ON_HAND += fill_water
    MILK_ON_HAND += fill_milk
    BEANS_ON_HAND += fill_beans
    CUPS_ON_HAND += fill_cups
    print("\nThe coffee machine has:")
    print("{} of water".format(WATER_ON_HAND))
    print("{} of milk".format(MILK_ON_HAND))
    print("{} of coffee beans".format(BEANS_ON_HAND))
    print("{} of disposable cups".format(CUPS_ON_HAND))
    print("{} of money".format(CASH_ON_HAND))

elif choice.lower() == "take":
    print("I gave you ${}".format(CASH_ON_HAND))
    CASH_ON_HAND = 0

    print("\nThe coffee machine has:")
    print("{} of water".format(WATER_ON_HAND))
    print("{} of milk".format(MILK_ON_HAND))
    print("{} of coffee beans".format(BEANS_ON_HAND))
    print("{} of disposable cups".format(CUPS_ON_HAND))
    print("{} of money".format(CASH_ON_HAND))
