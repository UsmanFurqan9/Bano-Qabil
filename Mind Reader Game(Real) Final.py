#mind reading trick game
#this game utilizes a mathematic logic 
#insturctions:
#just think of any number from 1 to 999
#enter the number you thought of
#the program will do all the maths and calculations for you and tell you the number you were thinking
#this program was made by Usman Furqan 
from time import sleep

print("Welcome To Mind Reader... ")
sleep(2)
X=input("Think of any number from 1 to 999: ")
print()
X=int(X)
sleep(2)
print("Multiply it by 2:",X,"x 2 =",X*2)
print()
X=X*2
sleep(4)
print("Now multiply your answer by 5: ",X,"x 5 =",X*5)
print()
X=X*5
sleep(4)
print ("Now subtract 5 from your answer:",X,"- 5 =",X-5)
print()
X=X-5
sleep(4)
print ("Finally add 7: ",X,"+ 7 =",X+7)
print()
X=X+7
sleep(2)
print ("\033[1mYour answer is:",X) 
sleep(2)
if X <= 92:
    print ("The first digit is the number you thought of and the second digit will always be the number 2.")
elif X <= 992:
    print("The first two digits are the numbers you thought of and the last digit will always be the number 2.")
elif X <= 9992:  
    print ("The first three digits are the numbers you thought of and the last digit will always be the number 2.")
sleep(2)
print ()
print ("This Game Was Made By Usman Furqan")