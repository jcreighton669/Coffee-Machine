digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine']
numeral = input()
numerals = list(numeral)
for i in range(len(numerals)):
    element = int(numerals[i])
    print(digits[element])
