import random as ran
ans='y'
ctr=0
while(ans=='y'):
    lit=int(input("Enter a limit:"))
    while(ctr<5):
        rand=ran.randint(1,lit)
        guess=int(input("Guess a number between 1 and {0}:".format(lit)))
        if(guess==rand):
            print("You Won!!")
            break
        else:
            ctr+=1
        if(not(ctr<5)):
            print("You lose!!\nThe number was:",rand)
    ans=input("do you want to play again(y or n):")
    if(ans=='y'):
        ctr=0
    else:
        print("thank you for playing")