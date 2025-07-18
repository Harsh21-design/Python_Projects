##   ROCK PAPER OR SCISSOR GAME
while True:
    import random
    def game(comp,you):
        if comp==you:
            return None
        elif comp=="rock":
            if you=="paper":
                return True
            elif you=="scissor":
                return False
        elif comp=="paper":
            if you=="scissor":
                return True
            elif you=="rock":
                return False
        elif comp=="scissor":
            if you=="rock":
                return True
            elif you=="paper":
                return False
    # print("Computer turn: Snake(s), Water(w) or Gun(g) ? ")
    print("Computer turn: Rock, Paper or Scissor ? ")
    randNo = random.randint(1,3)
    if randNo == 1:
        comp = "rock"
    elif randNo == 2:
        comp = "paper"
    elif randNo == 3:
        comp = "scissor"
    # you = input("Your turn: Snake(s), Water(w) or Gun(g) ? ")
    you = input("Your turn: Rock, Paper or Scissor ? ")
    g = game(comp,you) 
    print(f"Computer chose: {comp}")
    print(f"You chose: {you}")
    if you!="end":
        if(you!="rock" and you!="paper" and you!="scissor"):
                print("'Wrong choice!! Play Again'")
        elif g == None:
                print("Its a Draw! Play Again")
        elif g:
                print("You WIN!!")
        else:
                print("You LOSE!!")
        print("\n")
        print("Play Again or Enter 'end' for exit the Game!")
    print("*"*20)
    print("\n")
    if(you == "end"):
            print("Thanks for Playing.")
            break
    
    