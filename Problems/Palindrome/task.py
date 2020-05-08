# put your python code here
string = input()
string = list(string)

# print(string[::-1])
if string[:] == string[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
