import random
def play():
    player=input("'s' for scissors,'p' for paper , 'r' for rock\n")
    computer = random.choice(['r','p','s'])
    if player==computer:
        print('opponent got', computer)
        return 'it\'s a Tie'  
    if win(player,computer):
        print('opponent got',computer)
        return 'you won'
    if win(computer,player):
        print('opponent got',computer)   
        return'you lost'         
def win(player,computer):   
    if (player=='r'and computer=='s')or(player=='s'and computer=='p')or(player=='p'and computer=='r'): 
     return True
print(play())