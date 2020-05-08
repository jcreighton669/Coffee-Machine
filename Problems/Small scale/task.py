floats = []
nums = input()

while nums != '.':
    floats.append(float(nums))
    nums = input()

print(min(floats))
