column = int(input())
row = int(input())

if column < 8 and column > 1:
    if row < 8 and row > 1:
        print(8)
    elif row == 1 or row == 8:
        print(5)
elif column == 1 or column == 8:
    if row < 8 and row > 1:
        print(5)
    elif row == 1 or row == 8:
        print(3)
