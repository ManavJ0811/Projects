import random
import time
print("-------------NUMBER GUESSING GAME-----------------")
time.sleep(2)
name = str(input("What is your name "))
print(f"Welcome {name}!!")
time.sleep(2)
play = input("DO YOU WANT TO PLAY THIS GUESS GAME? ").lower()

if play == 'yes':
    print("cool! let's start the game")

elif play == 'no':
    quit()

else:
    quit()

up = (input("Give me a number for lower limit of range "))
time.sleep(1)
down = (input("Give me a number for upper limit of range "))

if up.isdigit and down.isdigit():
    up =int(up)
    down=int(down)
    
else:
    quit()
 
while True:
    rm = random.randint(up , down)
    
    guess = int(input("make a guess b/w your given number "))
    if guess >down:
        print("MAKE A LOWER GUESS")
        continue
    elif guess< up:
        print("MAKE A BIGGER GUESS")
    else: 
        time.sleep(1)   
        print(f"YOUR GUESS IS {guess} AND THE RANDOM NUMBER IS: {rm} ") 
    if guess == rm:
         print("YOU GOT IT!")
         break
         quit()  
    else:
        print("try agin")
        continue    






    


   


    

    
        

