print('Write how many ml of water the coffee machine has:')
water = int(input())
print('Write how many ml of milk the coffee machine has:')
milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
beans = int(input())
print('Write how many cups of coffee you will need:')
cups = int(input())

enough_water = water // 200
enough_milk = milk // 50
enough_beans = beans // 15

enough_for = [enough_water, enough_milk, enough_beans]

if min(enough_for) == cups:
    print('Yes, I can make that amount of coffee')
elif min(enough_for) < cups:
    print('No, I can make only' + str(min(enough_for)) + 'cups of coffee')
else:
    print('Yes, I can make that amount of coffee (and even ' + str(min(
        enough_for) - 1) + ' more than that)')
