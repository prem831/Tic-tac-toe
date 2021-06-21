import random

bloc = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def cdisplay(b):
    print('  ' + b[0][0] + '  |' + '  ' + b[0][1] + '  |' + '  ' + b[0][2])
    # print("   |   |")
    print("------------------")
    print('  ' + b[1][0] + '  |' + '  ' + b[1][1] + '  |' + '  ' + b[1][2])
    print("------------------")
    print('  ' + b[2][0] + '  |' + '  ' + b[2][1] + '  |' + '  ' + b[2][2])


def input1():
    temp1 = ""
    while temp1 not in (1, 2):
        temp1 = int(input("1. Play with system \n2. Multi user\nPlease enter your selection:"))
    return temp1


def input2(per):
    print(f"Now {per} turn")
    temp1 = ""
    while temp1 not in (1, 2, 3):
        temp1 = int(input("enter row no"))
    temp2 = ""
    while temp2 not in (1, 2, 3):
        temp2 = int(input("enter column no"))
    return temp1 - 1, temp2 - 1


def update_bloc(per):
    while True:
        n, m = input2(per)
        if bloc[n][m] == " ":
            break

    if per == "player1":
        bloc[n][m] = 'X'
    elif per in ["player2", "system"]:
        bloc[n][m] = 'O'
    else:
        print("no valid user")

    cdisplay(bloc)


def check_win(p):
    return (bloc[0][0] == bloc[0][1] == bloc[0][2] == p) or (bloc[1][0] == bloc[1][1] == bloc[1][2] == p) or (
            bloc[2][0] == bloc[2][1] == bloc[2][2] == p) or (bloc[0][0] == bloc[1][0] == bloc[2][0] == p) or (
                   bloc[0][1] == bloc[1][1] == bloc[2][1] == p) or (
                   bloc[0][2] == bloc[1][2] == bloc[2][2] == p) or (
                   bloc[0][0] == bloc[1][1] == bloc[2][2] == p) or (bloc[0][2] == bloc[1][1] == bloc[2][0] == p)


def reset_bloc():
    global bloc
    bloc = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("reset completed")


def system_update(gs):
    temp4 = []
    for i in range(3):
        for j in range(3):
            if gs[i][j] == " ":
                temp4.append([i, j])
    rs1, rs2 = random.choice(temp4)
    bloc[rs1][rs2] = 'O'
    print("Now system will play ")
    cdisplay(bloc)


def game1():
    cdisplay(bloc)
    print("X is first player      O is second player")
    temp3 = 1
    for i in range(1, 6):
        update_bloc("player1")
        if check_win("X"):
            print("you won the game")
            break
        if i >= 5:
            continue
        system_update(bloc)
        if check_win("O"):
            print("system won")
            break
    else:
        print("no one won")


def game2():
    cdisplay(bloc)
    print("X is first player      O is second player")
    temp3 = 1
    for i in range(1, 6):
        update_bloc("player1")
        if check_win("X"):
            print("Player 1 won the game")
            break
        if i >= 5:
            continue
        update_bloc("player2")
        if check_win("O"):
            print("Player 2 won the game")
            break

    else:
        print("no one won")


while True:
    reset_bloc()
    option1 = input1()
    if option1 == 1:
        game1()
    else:
        game2()
    cont = input("if you want play again enter YES else enter any key: ")
    if cont.upper() != "YES":
        break

print("Thank you for playing")
