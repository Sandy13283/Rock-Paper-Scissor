# # '''rock wins against scisor : 0 - Rock
# # scisor wins against paper   : 1 - Paper
# # paper wins against rock'''  : 2 - Scisor

# ''' 
# So there are total nine case we can take 
# (0,0),(1,1),(2,2) we avoide these because their is tie 
# (0,2),(1,2),(2,1) : You win
# (1,0),(2,0),(0,1) : Computer win
# Any other input : you lose
# '''
import random as R
X=int(input("Enter your Choice(0:Rock,1:Paper,2:Scisor) : "))
Y=R.randrange(0,3)
print(f"Computer Choice {Y}")
if X==Y :
    print("It's a Draw")
elif (X==0 and Y==2) or (X==1 and Y==2) or (X==2 and Y==1):
    print("You Win Bro, Party!\nParty!")
elif (X==1 and Y==0) or (X==2 and Y==0) or (X==0 and Y==1):
    print("You lose! \nComputer Win's ")
else:
    print("Invalid input,\nYou lose\nComputer Win's")
