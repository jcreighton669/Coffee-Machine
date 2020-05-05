# Write your code here
water_for_coffee = 200
milk_for_coffee = 50
beans_for_coffee = 15

cups_wanted = int(input("Write how many cups of coffee you will need: "))

water_needed = water_for_coffee * cups_wanted
milk_needed = milk_for_coffee * cups_wanted
beans_needed = beans_for_coffee * cups_wanted

print("For {} cups of coffee you will need:".format(cups_wanted))
print("{} ml of water".format(water_needed))
print("{} ml of milk".format(milk_needed))
print("{} g of coffee beans".format(beans_needed))
