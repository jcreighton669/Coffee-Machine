# put your python code here
room_one_students = int(input())
room_two_students = int(input())
room_three_students = int(input())



room_one_desks = room_one_students // 2 + room_one_students % 2
# print(room_one_desks)

room_two_desks = room_two_students // 2 + room_two_students % 2
# print(room_two_desks)

room_three_desks = room_three_students // 2 + room_three_students % 2
# print(room_three_desks)

print(int(room_one_desks + room_two_desks + room_three_desks))
