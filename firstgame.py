import random
print("******* Welcome To The SPS *********")
ch="y"
while(ch=="y"):
    w=0
    lo=0
    c=5
    i=1
    

    while(i<=c):
        l=["s","p","sc"]
        computer=random.choice(l)
        print("Press 's' for snake \n\t'p' for paper \n\t'sc' for scissor")
        a=input()
        print(computer)

        if a is computer:
            print("Close Encounter,But It's a Draw")
        elif ((a is "s" and computer is "p") or (a is "p" and computer is "sc") or (a is "sc" and computer is "s")):
            print("Sorry You Lost this round")
            lo=lo+1
        else :
            print("Bravo, You Won this Round.Keep it up")
            w=w+1
        i=i+1

    print("Your score Out Of 5 trials =",w)
    print("Computer score Out Of 5 trials =",lo)
    if w>lo :
        print("Winner Winner , SPS Dinner")
    elif w==lo:
        print("Boom Shakalaka , It's a tie")
    else:
        print("You Gotto improve your skills ")
    ch=input("Do you Wish to play Again \n 'y' 'n' ")
    continue
    


