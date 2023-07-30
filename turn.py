from dice import *
import random as r

def turn_new(players,player)
    nos=dice_roll()
    
    if (players[player][1] * players[player][2] * players[player][3] * players[player][4] == 0 and nos==6):
        t=players[player].index(0)
        players[player][t]=players[player][t]+1+(player*13)

    print("Players is at :\n")  
    print(players[player])  

    return players

def turn_complete(players,player):
    nos=dice_roll()
    for j in range(1,5):
        if(players[player][j]==51-(player*13) and nos==6):
            players[player][j]=58
                        

        elif(players[player][j]==58-nos-(player*13)):
            players[player][j]=58
        
            
    print("Players is at :\n")  
    print(players[player])  

    return players


def turn_move(players,player):
    nos=dice_roll
        
    for j in range(1,5):    
        if(players[player][j]==51-nos-(player*13)):
            players[player][j]=51-(player*13)
            return players
        
        elif ((players[player][j]+nos) not in players[player]):
            
            players[player][j]+=nos
            if (players[player][j]>52):
                players[player][j]-=52
                if (players[player][j] in players[player]):
                    players[player][j]=players[player][j]+52-nos
            
            return players
    
            
def turn_cap(players,player):
    temp=[]
    for j in range(len(players)):
        for k in range(1,4):
            for m in range(1,4):
                if (j==player):
                    continue
                if (players[player][m]==players[j][k] and players[player][m]<53 and players[player][m]>0):
                    players[j][k]=0
                    break










    












    


