min_sleep = int(input())
max_sleep = int(input())
real_sleep = int(input())

if min_sleep <= max_sleep:
    if real_sleep > max_sleep:
        print("Excess")
    elif real_sleep > min_sleep and real_sleep < max_sleep:
        print("Normal")
    elif real_sleep < min_sleep:
        print("Deficiency")
