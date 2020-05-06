# Write your code here
print("Write how many ml of water the coffee machine has:")
water_in_machine = int(input())

print("Write how many ml of milk the coffee machine has:")
milk_in_machine = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
beans_in_machine = int(input())

print("Write how many cups of coffee you will need:")
cups_wanted = int(input())

WATER_PER_CUP = 200
MILK_PER_CUP = 50
BEANS_PER_CUP = 15

water_needed = WATER_PER_CUP * cups_wanted
milk_needed = MILK_PER_CUP * cups_wanted
beans_needed = BEANS_PER_CUP * cups_wanted

water_cups_available = water_in_machine // water_needed
milk_cups_available = milk_in_machine // milk_needed
bean_cups_available = beans_in_machine // beans_needed

possible_cups = min(water_cups_available, milk_cups_available, bean_cups_available)

if possible_cups == cups_wanted:
    print("Yes, I can make that amount of coffee")
elif possible_cups < cups_wanted:
    print("No, I can make only {} cups of coffee".format(possible_cups))
elif possible_cups > cups_wanted:
    print("Yes, I can make that amount of coffee (and even {} more than that)"
          .format((possible_cups - cups_wanted)))

