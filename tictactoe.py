# Assignment: Tic-Tac-Toe
# Author: Danny Teeples

def grid(num_list):
    print(f"{num_list[0]}|{num_list[1]}|{num_list[2]}")
    print("-+-+-")
    print(f"{num_list[3]}|{num_list[4]}|{num_list[5]}")
    print("-+-+-")
    print(f"{num_list[6]}|{num_list[7]}|{num_list[8]}")

def choose_letter(letter,num_list):
    error = True
    while error == True:
        player1 = int(input(f"{letter}'s turn to choose a square (1-9):  "))
        for i in num_list:
            if i == player1:
                num_list[(i-1)] = letter
                error = False
    return num_list

def win(num_list):
    if num_list[0] == num_list[1] == num_list[2]:
        win = num_list[0]
    elif num_list[3] == num_list[4] == num_list[5]:
        win = num_list[3]
    elif num_list[6] == num_list[7] == num_list[8]:
        win = num_list[6]
    elif num_list[0] == num_list[3] == num_list[6]:
        win = num_list[0]
    elif num_list[1] == num_list[4] == num_list[7]:
        win = num_list[1]
    elif num_list[2] == num_list[5] == num_list[8]:
        win = num_list[2]
    elif num_list[0] == num_list[4] == num_list[8]:
        win = num_list[0]
    elif num_list[6] == num_list[4] == num_list[2]:
        win = num_list[6]
    else:
        win = "no"
    return win

def draw(num_list, player1, player2):
    draw = "yes"
    count = 0 
    for i in num_list:
        if i == player1 or i == player2:
            draw = "yes" 
        else:
            draw = "no"
            count =+ 1
    if count == 0:
        draw = "yes"
    else:
        draw = "no"
    return draw

def main():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1 = "x"
    player2 = "o"
    test_win = "no"
    test_draw = "no"
    while test_draw == "no" and test_win == "no":
        grid(num_list)
        print()
        num_list = choose_letter(player1,num_list)
        test_win = win(num_list)
        test_draw = draw(num_list, player1, player2)
        if test_win == "no" and test_draw == "no":
            grid(num_list)
            print()
            num_list = choose_letter(player2,num_list)
            test_win = win(num_list)
            test_draw = draw(num_list, player1, player2)
    grid(num_list)
    print()
    if test_draw == "yes":
        print("The game is a draw")
    else:
        print(f"The winner is {test_win}'s")

if __name__ == "__main__":
    main()