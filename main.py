import os
os.system("clear && figlet XO GAME")
X=os.system("figlet X")
O=os.system("figlet O")
print("""
p1==>X
p2==>O
1              ##2             ##3
               ##              ##
               ##              ##
               ##              ##
               ##              ##
################################################
4              ##5             ##6
               ##              ##
               ##              ##
               ##              ##
               ##              ##
################################################
7              ##8             ##9
               ##              ##
               ##              ##
               ##              ##
               ##              ##               
""")
u=input("p1 ==> ")
if u =="1":
    print("""
                   ##2             ##3
                   ##              ##
           p1      ##              ##
                   ##              ##
                   ##              ##
    ################################################
    4              ##5             ##6
                   ##              ##
                   ##              ##
                   ##              ##
                   ##              ##
    ################################################
    7              ##8             ##9
                   ##              ##
                   ##              ##
                   ##              ##
                   ##              ##               
    """)
