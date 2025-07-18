## GUESS THE CORRECT NUMBER ( 1 to 50 )
while True: 
    import random
    n = random.randint(1,51)
    a = 1
    g = 0 #Guesses
    

    while(a!=n):
        a = int(input("Enter a number(1-50): "))
        if(a>n):
            print("Wrong!! Enter a Smaller Number")
            g = g+1
        elif(a<n):
            print("Wrong!! Enter a Higher Number")
            g = g+1
        
    print(f"You guessed the correct number '{n}' in {g} guesses!!")
    