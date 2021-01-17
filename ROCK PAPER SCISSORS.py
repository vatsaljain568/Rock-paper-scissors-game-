        # ROCK PAPER SCISSORS  GAME
import random

def game(comp , you):
        if comp == you:
                return None
        elif comp == 'r':
                if you == 's':
                        return False
                elif you == 'p':
                        return True
        elif comp == 'p':
                if you == 's':
                        return True
                elif you == 'r':
                        return False
        elif comp == 's':
                if you == 'r':
                        return True
                elif you == 'p':
                        return False                
print("Comp turn : Rock(r) Paper(p) or Scissors(s)")
randno = random.randint(1,3)
if randno == 1:
        comp = 'r'
elif randno == 2:
        comp = 'p'
elif randno == 3:
        comp = 's'
you = input("Your turn: Rock(r) Paper(p) or Scssors(s)") 
a = game(comp , you)
print( f"Computer choose {comp}")
print( f"you choose {you}")
if a == None:
        print("Game is tie")
elif a:
        print(" You Win")
else :
        print(" You Lose")        

