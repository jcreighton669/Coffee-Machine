# put your python code here
cinema_halls = int(input())
ind_capacity = int(input())
planned_viewers = int(input())

available_seats = cinema_halls * ind_capacity

print(planned_viewers <= available_seats)
