#AW YEAH BATTLESHIP YEAH

#CISC106 Project
#Due Sunday, April 28
#Class Time: MWF 11:15
#TA: Mustafa Zengin
#Briana Lamet
#Justin Grier

import turtle
from random import *
from math import *

#-------------------------------------------------------
#-------------------------------------------------------
#TURTLE GRAPHICS HELPER CODES

#Water
def waves(): 
    turtle.speed(10)
    turtle.penup()
    turtle.width(3)
    turtle.color("blue")
    x=-400
    while x<400:
        turtle.goto(x,40*sin((x/100)*2*pi))
        turtle.pendown()
        x+=1
        
#Base of boat
def boat(a,l,r): #a=angle, l=length, r=rotations
    turtle.speed(10)
    turtle.color("grey") #ships are grey because war boats are metal and grey
    turtle.penup()
    turtle.goto(100,0)
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    d = a/r #d = degree
    while r>0:
        turtle.forward(l)
        turtle.right(d)
        r-=1
    turtle.end_fill()

#Mast of boat
def mast():
    turtle.penup()
    turtle.goto(-20,-10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(-20,150)
    turtle.left(90)
    turtle.goto(-45,150)
    turtle.left(90)
    turtle.goto(-45,-10)
    turtle.end_fill()

#Sail of boat
def sail():
    turtle.penup()
    turtle.color("black")
    turtle.goto(-20,150)
    turtle.width(3)
    turtle.pendown()
    turtle.goto(60, 45)
    turtle.goto(-20,50)
    
#Explosion for sunken ship    
def boom():
    turtle.penup()
    turtle.width(1)
    turtle.speed(10)
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    return


#Graphic for when User sinks one of Computer's ships

def usersink(x): #x is the type of ship
    x = shiptype(x)
    turtle.reset()
    turtle.speed(10)
    waves(); boat(180, 4, 100); mast(); sail(); boom()
    turtle.penup()
    turtle.width(1)
    turtle.color("black")
    turtle.goto(-200, 200)
    turtle.pendown
    turtle.write("You sank the Computer's "+str(x)+"!",font=("Arial",24,"normal"))
    turtle.penup()
    turtle.color("white")


#-------------------------------------------------------
#-------------------------------------------------------
    
#Board Grids Helper Codes

def zero(x):
    zerolist = ["0"]*x #create a list with x number of 0's
    return(zerolist)

def zero2(x):
    nestedlist=[zero(x)] #set nested list as x number of 0s
    for y in range(x-1): #for one less times than x (because first index is 0)
        nestedlist.append(zero(x));#insert the zero list into the nested list
    return(nestedlist)

#Creating Empty Game Board
def emptyboard():
    board = zero2(10) #we have 10 lists with 10 zeros
    return(board)


#Printing Board as a Grid (x = board)
def grid(x): 
    y=0
    top = list("abcdefghij")
    print ("      " + "    ".join( str(x) for x in top)) 
    n=1
    while y<10:
        while n<10:
            print(n," ",x[y]) #print every item in the board list on a new line
            y+=1 #that way it looks like an actual battleship board
            n+=1
        print(n,"",x[y])
        y+=1
    return(x)

#-------------------------------------------------------
#-------------------------------------------------------

#GLOBAL VARIABLES ESTABLISHED NOW.
bombs = []
userboard = emptyboard()
compboard = emptyboard()
bombboard = emptyboard()
usersunken = []
compsunken = []

#-------------------------------------------------------
#-------------------------------------------------------

#GAME HELPER CODES

#SHIPS
#Battleship B(4) : DONE
#Destroyer = D(3) : DONE
#Aircraft Carrier = A(5) : DONE
#Submarine = S(3) : DONE
#PT Boat = P(2) : DONE

#Converting letter input to list index
def lettercoordinate(b):
    if b == "a": return 0 #indices start at zero
    if b == "b": return 1
    if b == "c": return 2
    if b == "d": return 3
    if b == "e": return 4
    if b == "f": return 5
    if b == "g": return 6
    if b == "h": return 7
    if b == "i": return 8
    if b == "j": return 9

#Determining type of ship
def shiptype(x):
    if x=="P": return "PT Boat"
    if x=="S": return "Submarine"
    if x=="D": return "Destroyer"
    if x=="B": return "Battleship"
    if x=="A": return "Aircraft Carrier"

#-------------------------------------------------------
#-------------------------------------------------------

#USER BOARD
#Code for user to input their ships

def userships():
    print("\n Prepare to deploy your fleet in unknown waters.\n")
    
    #AIRCRAFT CARRIER (5)
    a1 = input("What number does your Aircraft Carrier start on? (Length 5) ") #list number
    while (a1!="1")and(a1!="2")and(a1!="3")and(a1!="4")and(a1!="5")and(a1!="6")and(a1!="7")and(a1!="8")and(a1!="9")and(a1!="10"):
        print("Invalid input. Try again.")
        a1 = input("What number does your Aircraft Carrier start on? (Length 5) ")
    a = int(a1)-1 #subtract one because list index starts at 0
    b1 = input("What letter does your Aircraft Carrier start on? (Length 5) ") #position inside list
    while (b1!="a")and(b1!="b")and(b1!="c")and(b1!="d")and(b1!="e")and(b1!="f")and(b1!="g")and(b1!="h")and(b1!="i")and(b1!="j"):
        print("Invalid input. Try again.")
        b1 = input("What letter does your Aircraft Carrier start on? (Length 5) ")
    b = lettercoordinate(b1)
    direction = input("Is your Aircraft Carrier vertical or horizontal? ")
    while (direction != "vertical") and (direction != "horizontal"):
        print("Invalid input. Try again.")
        direction = input("Is your Aircraft Carrier vertical or horizontal? ")
    if direction == "vertical":
        length=0
        while length<4:
            userboard[a][b]="A"
            a+=1 ; length+=1
    if direction == "horizontal":
        length=0
        while length<4:
            userboard[a][b]="A"
            b+=1 ; length+=1
    print("\n \t \t - USER BOARD - \n")
    grid(userboard)
            
    #BATTLESHIP (4)
    a1 = input("\nWhat number does your Battleship start on? (Length 4) ") #list number
    while (a1!="1")and(a1!="2")and(a1!="3")and(a1!="4")and(a1!="5")and(a1!="6")and(a1!="7")and(a1!="8")and(a1!="9")and(a1!="10"):
        print("Invalid input. Try again.")
        a1 = input("What number does your Battleship start on? (Length 4) ") 
    a = int(a1)-1 
    b1 = input("What letter does your Battleship start on? (Length 4) ") #position inside list
    while (b1!="a")and(b1!="b")and(b1!="c")and(b1!="d")and(b1!="e")and(b1!="f")and(b1!="g")and(b1!="h")and(b1!="i")and(b1!="j"):
        print("Invalid input. Try again.")
        b1 = input("What letter does your Battleship start on? (Length 4) ")
    b = lettercoordinate(b1)
    direction = input("Is your Battleship vertical or horizontal? ")
    while (direction != "vertical") and (direction != "horizontal"):
        print("Invalid input. Try again.")
        direction = input("Is your Battleship vertical or horizontal? ")
    if direction == "vertical":
        length=0
        while length<4:
            userboard[a][b]="B"
            a+=1 ; length+=1
    if direction == "horizontal":
        length=0
        while length<4:
            userboard[a][b]="B"
            b+=1 ; length+=1
    print("\n \t \t - USER BOARD - \n")
    grid(userboard)

    #DESTROYER (3)
    a1 = input("\nWhat number does your Destroyer start on? (Length 3) ") #list number
    while (a1!="1")and(a1!="2")and(a1!="3")and(a1!="4")and(a1!="5")and(a1!="6")and(a1!="7")and(a1!="8")and(a1!="9")and(a1!="10"):
        print("Invalid input. Try again.")
        a1 = input("What number does your Destroyer start on? (Length 3) ")        
    a = int(a1)-1 
    b1 = input("What letter does your Destroyer start on? (Length 3) ") #position inside list
    while (b1!="a")and(b1!="b")and(b1!="c")and(b1!="d")and(b1!="e")and(b1!="f")and(b1!="g")and(b1!="h")and(b1!="i")and(b1!="j"):
        print("Invalid input. Try again.")
        b1 = input("What letter does your Destroyer start on? (Length 3) ")
    b = int(lettercoordinate(b1))
    direction = input("Is your Destroyer vertical or horizontal? ")
    while (direction != "vertical") and (direction != "horizontal"):
        print("Invalid input. Try again.")
        direction = input("Is your Destroyer vertical or horizontal? ")
    if direction == "vertical":
        length=0
        while length<3:
            userboard[a][b]="D"
            a+=1 ; length+=1
    if direction == "horizontal":
        length=0
        while length<3:
            userboard[a][b]="D"
            b+=1 ; length+=1
    print("\n \t \t - USER BOARD - \n")
    grid(userboard)

    #SUBMARINE (3)
    a1 = input("\nWhat number does your Submarine start on? (Length 3) ") #list number
    while (a1!="1")and(a1!="2")and(a1!="3")and(a1!="4")and(a1!="5")and(a1!="6")and(a1!="7")and(a1!="8")and(a1!="9")and(a1!="10"):
        print("Invalid input. Try again.")
        a1 = input("What number does your Submarine start on? (Length 3) ")        
    a = int(a1)-1 
    b1 = input("What letter does your Submarine start on? (Length 3) ") #position inside list
    while (b1!="a")and(b1!="b")and(b1!="c")and(b1!="d")and(b1!="e")and(b1!="f")and(b1!="g")and(b1!="h")and(b1!="i")and(b1!="j"):
        print("Invalid input. Try again.")
        b1 = input("What letter does your Submarine start on? (Length 3) ")
    b = int(lettercoordinate(b1))
    direction = input("Is your Submarine vertical or horizontal? ")
    while (direction != "vertical") and (direction != "horizontal"):
        print("Invalid input. Try again.")
        direction = input("Is your Submarine vertical or horizontal? ")
    if direction == "vertical":
        length=0
        while length<3:
            userboard[a][b]="S"
            a+=1 ; length+=1
    if direction == "horizontal":
        length=0
        while length<3:
            userboard[a][b]="S"
            b+=1 ; length+=1
    print("\n \t \t - USER BOARD - \n")
    grid(userboard)
    
    #PT BOAT (2)
    a1 = input("\nWhat number does your PT boat start on? (Length 2) ") #list number
    while (a1!="1")and(a1!="2")and(a1!="3")and(a1!="4")and(a1!="5")and(a1!="6")and(a1!="7")and(a1!="8")and(a1!="9")and(a1!="10"):
        print("Invalid input. Try again.")
        a1 = input("What number does your PT boat start on? (Length 2) ")
    a = int(a1)-1 
    b1 = input("What letter does your PT boat start on? (Length 2) ") #position inside list
    while (b1!="a")and(b1!="b")and(b1!="c")and(b1!="d")and(b1!="e")and(b1!="f")and(b1!="g")and(b1!="h")and(b1!="i")and(b1!="j"):
        print("Invalid input. Try again.")
        b1 = input("What letter does your PT boat start on? (Length 2) ")
    b = int(lettercoordinate(b1))
    direction = input("Is your PT boat vertical or horizontal? ")
    while (direction != "vertical") and (direction != "horizontal"):
        print("Invalid input. Try again.")
        direction = input("Is your PT Boat vertical or horizontal? ")
    if direction == "vertical":
        length=0
        while length<2:
            userboard[a][b]="P"
            a+=1 ; length+=1
    if direction == "horizontal":
        length=0
        while length<2:
            userboard[a][b]="P"
            b+=1 ; length+=1

#Function returns userboard
    return(userboard)


#-------------------------------------------------------
#-------------------------------------------------------

#COMPBOARD: DONE!

#Code for computer to randomly place ships.
#We need to randomly arrange the ships on the board so that none of them overlap
#The computer has to check that every spot where it wants to put the ship is empty
    #First spot must be empty, as well as every spot in the direction the ship will lay
    #Length of ship must not go off the board (index won't exist)
    #If there is anything in the way of the ship, it has to pick a new spot and run the check again

#HELPER CODE FOR PLACING COMPUTER SHIPS

def placeship(l,t): #l is length of ship, t is type as a string
    length = l

    #VERTICAL CODE : Works for ship of length 2, but not length 3.
    while l>0:
        a = randrange(0,9) #a is a random index 0-9, because it doesn't include 10
        b = randrange(0,9) #b is a random index 0-9
        direction = randrange(0,2) #direction is 0 or 1
        if direction == 0: #say 0 is vertical direction
            if compboard[a][b]=="0": #there is no ship at that spot
                if ((a+length)<10): #if the entire length of the ship is in range
                    flag = True
                    for h in range(length): #for every spot in the ship length
                        if compboard[a+h][b]!="0": #if that spot is taken
                            flag = False
                    if flag == True: #means all spots in length of ship are open
                        i = 0 #number of times you place your ship
                        while i<length:
                            compboard[a][b]= t #place a ship vertically
                            a+=1; i+=1 ; l=0 #a is where you place your ship
                            #after you place a ship, l=0, get out of the loop.
                            

    #HORIZONTAL CODE: Appears to be working for ship of length 2
        if direction == 1: #say 1 is horizontal direction
            if compboard[a][b]=="0": #there is no ship at that spot
                if ((b+length)<10): #if the entire length of the ship is in range
                    flag = True
                    for h in range(length): #for every spot in the ship length
                        if compboard[a][b+h]!="0": #if that spot is taken
                            flag = False
                    if flag == True: #means all spots in length of ship are open
                        i = 0 #number of times you place your ship
                        while i<length:
                            compboard[a][b]= t #place a ship vertically
                            b+=1; i+=1 ; l=0 #b is where you place your ship
                            #after you place a ship, l=0, get out of the loop.
#-------------------------------------------------------

#Function for Computer randomly placing ships on board
                            
def compships():
    placeship(2,"P") #PT BOAT (2)
    placeship(3,'S') #SUBMARINE (3)
    placeship(3,"D") #DESTROYER (3)
    placeship(4,"B") #BATTLESHIP (4)
    placeship(5,"A") #AIRCRAFT CARRIER (5)
    '''#PRINT COMPBOARD GRID (printed for now to check)
    print("\n \t \t - COMPUTER BOARD - \n")
    grid(compboard)''' #Printing computer board hidden for authentic gameplay
#Function Returns compboard
    return(compboard)


#-------------------------------------------------------
#-------------------------------------------------------
#USER SENDING BOMBS:DONE


#GUESSING SYSTEM
#User inputs 2 coordinates to send bomb
#Check if compboard has a ship at that spot
#If so, display graphic of hitting ship (name depends on P, S, D, B, or A at spot)
    #Need a loop that adds appropriate stars for each hit on each boat
    #Max hits is one less than length of boat
#If spot is empty, print "You missed"
#Add X to bomb board for hit
#Add / to bomb board for miss
#Replace ship letter on comp board with X if hit
    #Search the board for letter, if the index does not exist, that ship is sunk.
    #However, we only want to show each ship being sunk ONCE, so once it's sunk don't do it again (loops)
    #Once a ship is sunk, stop checking for that ship.

def userbomb():
    a1 = input("\n What number will be fired upon? ") #list number
    while (a1!="1")and(a1!="2")and(a1!="3")and(a1!="4")and(a1!="5")and(a1!="6")and(a1!="7")and(a1!="8")and(a1!="9")and(a1!="10"):
        print("Invalid input. Try again.")
        a1 = input(" What number will be fired upon? ") 
    a = int(a1)-1 
    b1 = input(" What letter will be fired upon? ") #position inside list
    while (b1!="a")and(b1!="b")and(b1!="c")and(b1!="d")and(b1!="e")and(b1!="f")and(b1!="g")and(b1!="h")and(b1!="i")and(b1!="j"):
        print("Invalid input. Try again.")
        b1 = input(" What letter will be fired upon? ") 
    b = lettercoordinate(b1)
    ships = ['P','S','D','B','A']

#MISS: Works
    if compboard[a][b]=="0":
        bombboard[a][b]='/' #put a / on the user bomb tracking board at that spot
        print("\nYou missed the enemy vessels. \n")
        
    #PRINT BOMB BOARD AS A GRID:
        print("\n \t     - USER BOMBING TRACKING BOARD - ")
        print("\t (Miss shown as '/' Hit shown as 'X') \n")
        grid(bombboard)
        

#HIT:Works
    for letter in ships: #check for every type of ship
        if letter in compboard[a][b]: #if a letter is in that spot
            x = shiptype(compboard[a][b]) #convert letter to ship name
            print("\n Your bombing in enemy waters was a success!\nYou've struck and enemy ship!")
            hit = True
            bombboard[a][b] = 'X' #put X on bomb tracking board
            compboard[a][b] = '0' #go to that same spot on compboard and change it to 'O'
            if hit == True:
                #PRINTING BOMB BOARD AS A GRID:
                print("\n \t     - USER BOMBING TRACKING BOARD - ")
                print("\t (Miss shown as '/' Hit shown as 'X') \n")
                grid(bombboard)

'''#SHOW COMPBOARD GRID TO CHECK HITS/MISSES ARE HAPPENING CORRECTLY
    print("\n \t \t - COMPUTER BOARD - \n")
    grid(compboard)'''
        


#When you hit the computer's ship
#Change ship letter to a '0'
        #Run checks for each type of ship
        #for ship in (ships = ['P','S','D','B','A'])
        #If there are no B's then battleship is sunk, etc.
        #If whole board is '0's then user won

#-------------------------------------------------------
#-------------------------------------------------------
    
#COMPUTER SENDING BOMBS CODE: DONE
        
#Computer cannot send a bomb to the same spot twice
        #Computer chooses random coordinates to send a bomb to
    #If there is not ship, computer missed and put / on userboard in that spot
    #add coordinate to "comp bombs list", do not allow comp to use same coordinates twice

#When the computer hit's a user's boat, change that spot to an X.
        #When the user's board is all '0's and 'X's the computer has won.



def compbomb():
    ships = ['P','S','D','B','A']
    bombsent = 0
    #must develop first bomb coordinate outside of loop
    a = randrange(0,9)
    b = randrange(0,9)
    while bombsent != True:
        if [a,b] not in bombs: #if the coordinate has not already been used
            #COMPUTER MISS: WORKS
            if userboard[a][b] == '0': #if there is no ship in that spot
                userboard[a][b] = '/' #put a / on the userboard to show where the comp sent a bomb
                bombs.append([a,b]) #add that coordinate to the bombs list
                print("\n The enemy has failed to strike your fleet.")

            #COMPUTER HIT: WORKS
            for letter in ships: #check for every type of ship
                if letter in userboard[a][b]: #if a letter is in that spot
                    x = shiptype(userboard[a][b]) #convert letter to ship name
                    print("\n The enemy has torpedoed your " + str(x) + "!")
                    bombs.append([a,b]) #add coordinate to bombs list
                    userboard[a][b] = 'X' #change ship letter on userboard to X
               
            #If a hit or a miss is accomplished, indicate a bomb has been sent.
            bombsent = True
                    
        #if [a,b] has already been used, generate new coordinates and try again
        a = randrange(0,9)
        b = randrange(0,9)
                
    #PRINT USER BOARD GRID AFTER EACH COMPBOMB
    print("\n \t \t - USER BOARD - \n")
    grid(userboard)


#-------------------------------------------------------    
#-------------------------------------------------------
    
    
#Searching an entire board for the presence of a specific letter.
    
def lettersearch(x,b): #x is letter, b is board
    check = False #assume boat is not there
    for element in b: #check every space in the board
        if x in element: #if the letter in that place
            check = True #the boat is in the board
    return(check)

#-------------------------------------------------------
#-------------------------------------------------------

#Checking User's board for sunken ships.

def usercheck():
    pcheck = lettersearch('P',userboard) #search the board for PT board
    if 'P' not in usersunken: #if P is not already indicated as underwater
        if pcheck == False: #if P is not there
            usersunken.append('P')
            print('\nThe enemy sank your PT Boat!\n There are no survivors.')

    scheck = lettersearch('S',userboard)
    if 'S' not in usersunken:
        if scheck == False:
            usersunken.append('S')
            print('\nThe enemy sank your Submarine!\nAll decks have been compromised.\nEstimated chance of survival: 0%')

    dcheck = lettersearch('D',userboard)
    if 'D' not in usersunken:
        if dcheck == False:
            usersunken.append('D')
            print('\nThe enemy sank your Destroyer!\nYou will be severely outgunned now.')

    bcheck = lettersearch('B',userboard)
    if 'B' not in usersunken:
        if bcheck == False:
            usersunken.append('B')
            print('\nThe enemy sank your Battleship!\nCasualties estimated to be over 1000.\nChances of mission success have dropped by 50%.')

    acheck = lettersearch('A',userboard)
    if 'A' not in usersunken:
        if acheck == False:
            usersunken.append('A')
            print('\nThe enemy sank your Aircraft Carrier!\nYour fleet has lost an aerial advantage.\nRescue boats have been sent to retrieve survivors.')
#-------------------------------------------------------

#Checking Computer's board for sunken ships.
            
def compcheck():
    pcheck = lettersearch('P',compboard) 
    if 'P' not in compsunken: 
        if pcheck == False: 
            compsunken.append('P')
            print("\nYou sank the enemy's PT Boat!\nNo surviving crewmen detected.")
            usersink('P')

    scheck = lettersearch('S',compboard)
    if 'S' not in compsunken:
        if scheck == False:
            compsunken.append('S')
            print("\nYou sank the enemy's Submarine!\nTheir fleet has lost the element of surprise.")
            usersink('S')

    dcheck = lettersearch('D',compboard)
    if 'D' not in compsunken:
        if dcheck == False:
            compsunken.append('D')
            print("\nYou sank the enemy's Destroyer!This will leave them outgunned to your superior firepower.")
            usersink('D')

    bcheck = lettersearch('B',compboard)
    if 'B' not in compsunken:
        if bcheck == False:
            compsunken.append('B')
            print("\nYou sank the enemy's Battleship!\nTheir command is in disarray, giving you a tactical advantage.")
            usersink('B')

    acheck = lettersearch('A',compboard)
    if 'A' not in compsunken:
        if acheck == False:
            compsunken.append('A')
            print("\nYou sank the enemy's Aircraft Carrier!\nThey suffered casualties upward of 3000.\nTheir fleet will be busy rescuing survivors. ")
            usersink('A')

#-------------------------------------------------------              
#-------------------------------------------------------

def comparelists(x): #x is your input list
    same = False #assume they do not contain the same elements
    x = set(x)
    y = set(['P','S','D','B','A'])
    if x==y: #if the elements in x are the same as the elements in y
        same = True
    return(same)

#-------------------------------------------------------
#-------------------------------------------------------
                
#BATTLESHIP GAME:

    #Computer places random ships.
    #Print intro.
    #User places random ships.
    #Print rules.
    #User sends first bomb
    #Need to code a loop that will alternate compbomb and userbomb until someone wins.
        #For the game. winner = 0. while winner == 0 run game, when someone wins set winner to comp or user.
        #If winner == user display "You won!" if winner==comp display "YOU HAVE BEEN DEFEATED. YOU SUCK."
    #Return winner (graphic maybe?)
    #Game ends.


def game():
    input("Welcome to the FleetCom BattleNet.\nToday, you are in command of a standard patrol fleet, doing recon in the South Pacific.\nPress ENTER to view details.")
    input("\nBriefing: At 0200 hours, 5 enemy vessels were detected heading towards your position.\nThe fleet is similar in size and type as your own, so the odds are even in an open water bombardment.\nHowever, your radar is being jammed by an unknown source making you unable to see the enemy vessel location.\n\nYour objective is to eliminate the enemy fleet and bring your crew home.\n\nDo You Accept Command of this Fleet? ")
    compboard = compships() #computer places ships
#PRINT EMPTY USERBOARD GRID
    userboard = emptyboard()
    print("\n \t \t - USER BOARD - \n")
    grid(userboard)
#Print Intro
    print("\nPhase One: Ship Placement\n")
    print("\nYou have 5 ships in your fleet: a PT boat (Length 2), a Submarine (Length 3),a Destroyer (Length 3), a Battleship (Length 4), and an Aircraft carrier (Length 5).")
    print("\nThe 'user board' shows the grid of the water in which you will place your ships.\nThe enemy has placed it's own fleet of identical ships on an identical board, which will remain hidden from you.")
    print("\nYou will be asked what letter and number you want your ship to start on, and then if you want it to lay vertically or horizontally.\nAll input letters must be lowercase!")
    print("\nYou may only choose the coordinates of each ship once, so choose carefully.\nYou may not place your ships on top of each other, or outside the confines of the board grid.If you do, your crew will die and you will lose.")
    input("\nIf you fail to perform correctly, you will automatically lose and will need to restart the battle.(i.e. if you input an invalid response, the simulation will end)\nPress ENTER to begin placement. ")
    #Let user place ships
    userboard = userships() #user places ships
#Print rules
    print("\nPhase Two:Warfare Tactics\n")
    print("\nNow that your fleet is in position, you are ready to begin assualting the enemy.\n")
    print("\nSelecting a number and letter on the grid will let your ships fire a barrage of 120mm shells at that spot in enemy territory.")
    print("\nThe 'User Bombing Tracking Board' will show you the grid of enemy waters, and where you have missed and hit enemy vessels.\n The 'User Board' will show you the locations of your ships and where the enemy has tried to (or successfully) hit.")
    print("\nAny vessel is sunk once the number of hits it takes are equal to that of its length.\n")
    input("Victory is obtained when you have successfully sunk the entire enemy's fleet.\nHaving all your ships sunk before all of the enemys will result in failure.\nFailure is NOT ACCEPTABLE.\n\nPress ENTER to begin assult. ")
    #Print Bomb Tracking Board above Userboard
    print("\n \t     - USER BOMBING TRACKING BOARD - ")
    print("\t (Miss shown as '/' Hit shown as 'X') \n")
    grid(bombboard)
    print("\n \t \t - USER BOARD - \n")
    grid(userboard)
    winner = 0
#Begin Bombing
    print("\n Setup Complete.Commence shelling in enemy territory. Good Luck. \n")
    while winner == 0:
        u = False #indicates all user ships are alive
        c = False #indicates all comp ships are alive
        while ((u==False) or (c==False)) and (winner==0):
            userbomb() ; compcheck() #user sends bomb, check for sunken compships
            c = comparelists(compsunken) #check if all comp ships have been sunken 
            if c==True: #if all compships have been sunken
                winner = "User" #the user won
                
            compbomb() ; usercheck() #comp sends bomb, check for sunken userships
            u = comparelists(usersunken) #check if all user ships have been sunken         
            if u==True: #if all user ships have been sunken
                winner = "Enemy"


    if winner == "Enemy":
        return(print("\n Your fleet has been decimated by the enemy ships.\nThousands of your crew have been reported K.I.A.\nYou have lost. Game over."))
    if winner == "User":
        return(print("\n Congratulations! All enemy ships have been destroyed and there is no sign of survivors.\nSimualation Complete: You are victorious in battle!"))

game() #Run game.

#-------------------------------------------------------
#-------------------------------------------------------

#FINISHING UP
#Add winner/loser graphics.
#Add function that prevents the user from giving invalid input.
#If invalid input, ask again.
