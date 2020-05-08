sum = 0
count = 1
numeral = input()

while numeral.lstrip('-+').isdigit():
    sum += float(numeral)
    numeral = input()
    if numeral == '.':
        break
    else:
        count += 1

print(sum / count)
