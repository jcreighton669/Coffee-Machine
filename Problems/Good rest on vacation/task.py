# put your python code here
num_days = int(input())
food_per_day = int(input())
flight_cost = int(input())
hotel_per_day = int(input())

total_cost = 2 * flight_cost + (num_days * food_per_day) + ((num_days - 1) * hotel_per_day)
print(total_cost)
