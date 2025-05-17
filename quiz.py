import time 
print("-----------------HI! WELCOME TO THE QUIZ GAME.-------------------")
play = input("DO YOU WANT TO PLAT THIS GAME?").lower()
if play == "yes":
    print("Great! LET'S START.")
else:
    quit()
score = 0
answers = input("What is the capital of india? ").lower()
if answers == "delhi":
    print("CORRECT!!!")
    score += 1
else:
    print("oops! WRONG ANSWER:(")

answers = input("What is the capital of UTTAR PRADESH? ").lower()
if answers == "lucknow":
    print("CORRECT!!!")
    score += 1
else:
    print("oops! WRONG ANSWER:( ")

answers = input("What is water in solid form called? ").lower()
if answers == "ice":
    print("CORRECT!!!")
    score += 1
else:
    print("oops! WRONG ANSWER:(")
 
answers = input("What comes after 1234? ").lower()
if answers == "5":
    print("CORRECT!!!")
    score += 1
else:
    print("oops! WRONG ANSWER:( ")

answers = input("HOW MANY TOTAL ALPHABETS ARE THERE? ").lower()
if answers == "26":
    print("CORRECT!!!")
    score += 1
else:
    print("oops! WRONG ANSWER:(")

print("ALL THE QUESTIONS ARE OVER. LET'S SEE THE RESULTS: ")
time.sleep(2)
print("YOUR TOTAL SCORE IS......")
time.sleep(3)
print(f"......{score}.....")

if score <= 2:
    print("YOU NEED TO WORK HARD!")

else:
    print("GREAT JOB!")