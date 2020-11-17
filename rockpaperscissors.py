
rock = "R"
paper = "P"
scissors = "S"

player1 = input("Input Option:")
player2 = input("Input Option:")

if player1 == rock and player2 == scissors:
    print("Player One Wins")
elif player1 == rock and player2 == paper:
    print("Player Two Wins")
elif player1 == rock and player2 == rock:
    print("Its a Draw")
elif player2 == rock and player1 == scissors:
    print("Player Two Wins")
elif player2 == rock and player1 == paper:
    print("Player One Wins")
elif player2 == rock and player1 == rock:
    print("Its a Draw")
else:
    print("Incorrect Input")

