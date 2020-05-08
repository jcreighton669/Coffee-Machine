scores = input().split()
# put your python code here
incorrect_count = 0
correct_count = 0

for i in scores:
    if i == 'I':
        incorrect_count += 1
    elif i == 'C':
        if incorrect_count < 3:
            correct_count += 1
        else:
            continue

if incorrect_count < 3:
    print("You won")
else:
    print("Game over")
print(correct_count)

