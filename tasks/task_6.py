
N = int(input("Введите N: "))
x, y = 0, 0
for i in range(1, N + 1):
    move = input(f"Ход {i}: ").strip().lower()
    steps = int(input("Количество шагов: "))

    if move == "вверх":
        y += steps
    elif move == "вниз":
        y -= steps
    elif move == "вправо":
        x += steps
    elif move == "влево":
        x -= steps
    else:
        print("Неверное направление, попробуйте снова")
        i -= 1
shortest_distance = abs(x) + abs(y)
print(shortest_distance)



# Your code here (˶ˆᗜˆ˵)