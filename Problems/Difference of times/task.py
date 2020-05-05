# put your python code here

first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())

first_time = (first_hours * 3600) + (first_minutes * 60) + first_seconds

second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())

second_time = (second_hours * 3600) + (second_minutes * 60) + second_seconds

time_elapsed = second_time - first_time
print(time_elapsed)
