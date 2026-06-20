def ft_count_harvest_recursive():
    def recursion(time, day):
        if (time == 0):
            print("Harvest time!")
        else:
            print(f"Day {day}")
            day += 1
            time -= 1
            recursion(time, day)
    time = int(input("Days until harvest: "))
    day = 1
    recursion(time, day)
