limit = int(input())
list = []
sevens_list = []

for i in range(limit):
    element = int(input())
    list.append(element)

for i in list:
    if i % 7 == 0:
        sevens_list.append(i ** 2)

for i in sevens_list:
    print(i)
