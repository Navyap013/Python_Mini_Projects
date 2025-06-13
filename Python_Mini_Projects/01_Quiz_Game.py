play=input("Hey do you wanna play? \n")  
if play.lower()=="yes":
    print("Ok,Let's Start :) ")
else:
    quit()

score=0

answer = input("What does DSA stands for? ")
if answer.lower() == "data structures and algorithm":
    print('Correct!')
    score+=1
else:
    print("Incorrect")  


answer = input("What does OOP stands for? ")
if answer.lower() == "object oriented programming":
    print('Correct!')
    score+=1
else:
    print("Incorrect")  


answer = input("What does CN stands for? ")
if answer.lower() == "computer networks":
    print('Correct!')
    score+=1
else:
    print("Incorrect")      


answer = input("What does DBMS stands for? ")
if answer.lower() == "data base management system":
    print('Correct!')
    score+=1
else:
    print("Incorrect")     


answer = input("What does OS stands for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score+=1
else:
    print("Incorrect")       


answer = input("What does FSD stands for? ")
if answer.lower() == "full stack development":
    print('Correct!')
    score+=1
else:
    print("Incorrect")        
      

print("Your total score is " + str(score) + " :)")
print("Your total percentage is " + str((score/6)*100) + "%")
