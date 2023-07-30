from checkend import *

def game(players):
    num=len(players)
    
    i=0
    while(1):
                  
        players=turn(players,i)
        if (check(players,i)==1):
            break
        i+=1
        if (i==num):
            i=0
    print("Game over\n")
    print("Winner :")
    print(i)


#preveting a self-block
#    for i in range(1,5):
#        if (players[player][i]==1+(player*13)):
            


