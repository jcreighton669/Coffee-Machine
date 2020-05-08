# put your python code here
numeral = int(input())
sum = 0
squares_sum = 0
while True:
    sum += numeral
    squares_sum += (numeral ** 2)
    numeral = int(input())
    if sum == 0:
        break

print(squares_sum)
