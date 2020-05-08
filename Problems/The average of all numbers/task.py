# put your python code here
low = int(input())
high = int(input())
sum = 0
count = 0

for i in range(low, high + 1):
    if i % 3 == 0:
        sum += i
        count += 1

print(sum / count)
