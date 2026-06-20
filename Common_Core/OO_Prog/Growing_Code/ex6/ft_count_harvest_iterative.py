def ft_count_harvest_iterative():
    time = int(input("Days until harvest: "))
    day = 1
    while (time > 0):
        print(f"Day {day}")
        day += 1
        time -= 1
    print("Harvest time!")
