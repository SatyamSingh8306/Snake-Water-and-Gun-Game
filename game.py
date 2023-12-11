'''hii there,
             my self satyam '''
#my first game program
import random
def gamewin(comp, you):
    if comp == you:
        return None
    elif comp =='s':
        if you=='w':
            return False
        elif you=='g':  
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("computer turn : snake(s) water(w) or gun(g)?")
randno = random.randint(1,3)
if randno==1:
    comp= 's'
elif randno ==2:
    comp='w'
elif randno == 3:
    comp='g'
you = input("you turn : snake(s) water(w) or gun(g)?")
print(f"computer choose: {comp}")
print(f"you choose: {you}")
a = gamewin(comp,you)
if a==None:
    print(f"the game is tie")
elif a == True:
    print("you win")
elif a==False:
    print("you loose")


