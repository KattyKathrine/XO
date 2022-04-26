a = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def coord_request(sym):
    x = int(input(f"Игрок {sym}, введите координату по горизонтали:\n"))
    if not 0 <= x <= 2:
        return ()
    y = int(input(f"Игрок {sym}, введите координату по вертикали:\n"))
    if not 0 <= y <= 2:
        return ()
    return x, y


def print_output():
    output = (
        f'  0 1 2\n'
        f'0 {a[0][0]} {a[0][1]} {a[0][2]}\n'
        f'1 {a[1][0]} {a[1][1]} {a[1][2]}\n'
        f'2 {a[2][0]} {a[2][1]} {a[2][2]}\n'

    )
    print(output)


def check_win():
    b = [[], [], [], [], [], [], [], []]
    for i in range(3):
        for j in range(3):
            if i == j:
                b[0].append(a[i][j])
            if i + j == 2:
                b[1].append(a[i][j])
            if i == 0:
                b[2].append(a[i][j])
            if i == 1:
                b[3].append(a[i][j])
            if i == 2:
                b[4].append(a[i][j])
            if j == 0:
                b[5].append(a[i][j])
            if j == 1:
                b[6].append(a[i][j])
            if j == 2:
                b[7].append(a[i][j])

    for i in range(8):
        if b[i][0] == b[i][1] and b[i][1] == b[i][2] and b[i][0] != "-":
            return b[i][0]
    return ""


player = "X"
reply = ()
winner = ""
cont = "Y"

print_output()

while True:
    if player == "X":
        reply = coord_request("X")
        while not reply:
            print("Такой позиции нет. Попробуйте еще:\n")
            reply = coord_request("X")
        while a[reply[0]][reply[1]] != "-":
            print("Позиция занята. Попробуйте еще:\n")
            reply = coord_request("X")
        a[reply[0]][reply[1]] = "X"
        player = "0"
        print_output()
        winner = check_win()
        if winner:
            print(f'Игрок {winner} победил.\n')
            break

    if "-" not in a[0] and "-" not in a[1] and "-" not in a[2]:
        cont = input("Победила дружба!\nВведите Y, чтобы сыграть еще раз, введите N, чтобы выйти:\n")
        if cont != "Y":
            break
        else:
            player = "X"
            a = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
            print_output()

    if player == "0":
        reply = coord_request("0")
        while not reply:
            print("Такой позиции нет. Попробуйте еще:\n")
            reply = coord_request("0")
        while a[reply[0]][reply[1]] != "-":
            print("Позиция занята. Попробуйте еще:\n")
            reply = coord_request("0")
        a[reply[0]][reply[1]] = "0"
        player = "X"
        print_output()
        winner = check_win()
        if winner:
            print(f'Игрок {winner} победил.\n')
            cont = input("Введите Y, чтобы сыграть еще раз, введите N, чтобы выйти:\n")
            if cont != "Y":
                break

print("Game over!")
