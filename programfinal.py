#Joel Lantigua 00294961
#programming for IT
#professor Penta
#12/19/21

#I have created 3 different games get through every level to win...

#game 1
#Inporting a random number
import random

num = random.randint(0, 22000)
turns = 0
state = False

#This command allows the user to take a guess and in return it tells the user whether the number is grater or less than the users input.
while not state:
    guess = int(input("Take a number guess from 0-22,000?:"))
    turns += 1
    if guess == num:
        state = True
        print(f"CONGRATS!! You found the number {num} after {turns} tries.")
    elif guess > num:
        print(f"The number you want is less than {guess}")
    else:
        print(f"The number you want is grater than {guess}")


print("Now Entering Level 2")

#game 2

secrets = ['programming', 'developers', 'hacker', 'python', 'building']
secret = random.choice(secrets)
tries = 14
display = '_'*len(secret)

stat = False
#This is tells the user that the have to guess a word and that they only have 14 attempts
while not stat:
    print('You are now going to guess a word and you only have ' + str(tries) + ' attempts left.')
    print(display)
    attempts = input('please enter a letter: ')
#This Command dislplays the correct letter that was guessed and the remaining with a blank space.
    a = 0
    if attempts in secret:
            while secret.find(attempts, a) != -1:
                a = secret.find(attempts, a)
                display = display[:a] + attempts + display[a + 1:]
                a += 1
            print('Good Job!')
    else:
        print('Damn try again.')
        tries -= 1

    if secret == display:
        print('Lets goooo! you win, the word was ' + secret)
        stat = True

    if tries == 0:
        print('Maybe Next Time! no attempts left')
        stat = True

#game3
print('Entering Level 3')
# starting a Tic-tac-toe game
#tinker is a method used to open a window to allow the game to run.
from tkinter import *
from tkinter import messagebox
import random as r

#This would be the games background.
def button(frame):          
    k=Button(frame,padx=1,bg="black",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return k

 #This allows the other player to have thier turn in the game
def change_a():             
    global a
    for l in ['O','X']:
        if not(l==a):
            a=l
            break
#this should allow the game to resets after its done.
def reset():                
    global a
    for l in range(3):
        for j in range(3):
                b[l][j]["text"]=" "
                b[l][j]["state"]=NORMAL
    a=r.choice(['O','X'])

#this command should check for which player wins the 3 in a row or if the match end in a tie.
def check():                
    for l in range(3):
            if(b[l][0]["text"]==b[l][1]["text"]==b[l][2]["text"]==a or b[0][l]["text"]==b[1][l]["text"]==b[2][l]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won 3 in a row")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won 3 in a row")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","OH WOW The match ended in a draw")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Turn")

#this part is the title of the game and which letter is used in the game which is X and O also shows the color they are.
root=Tk()                   
root.title("Tic-Tac-Toe")   
a=r.choice(['O','X'])       
colour={'O':"red",'X':"yellow"}
b=[[],[],[]]
for l in range(3):
        for j in range(3):
                b[l].append(button(root))
                b[l][j].config(command= lambda row=l,col=j:click(row,col))
                b[l][j].grid(row=l,column=j)
label=Label(text=a+"'s Turn",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()


