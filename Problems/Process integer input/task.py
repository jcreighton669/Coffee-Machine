# put your python code here
nums = []
num = int(input())

while True:
    if num >= 10 and num <= 100:
        nums.append(num)
    elif num > 100:
        break
    num = int(input())

for i in nums:
    print(i)
