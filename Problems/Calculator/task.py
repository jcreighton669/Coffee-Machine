# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()
answer = ""

if operation == "+":
    answer = first_number + second_number

elif operation == "-":
    answer = first_number - second_number

elif operation == "/":
    if second_number == 0:
        print("Division by 0!")
    else:
        answer = first_number / second_number

elif operation == "*":
    answer = first_number * second_number

elif operation == "mod":
    if second_number == 0:
        print("Division by 0!")
    else:
        answer = first_number % second_number

elif operation == "pow":
    answer = first_number ** second_number

elif operation == "div":
    if second_number == 0:
        print("Division by 0!")
    else:
        answer = first_number // second_number

print(answer)
