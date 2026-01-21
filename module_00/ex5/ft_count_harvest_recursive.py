def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    index = 1

    def ft_recursive(index):
        if index <= days:
            print(f"Day {index}")
            ft_recursive(index + 1)
        else:
            print("Harvest time!")
            return
    ft_recursive(index)
