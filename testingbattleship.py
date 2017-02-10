userboard =[['A', 'B', 'D', 'X', 'S', '0', '0', '0', '0', '0'],['A', 'B', 'D', 'X', 'S', '0', '0', '0', '0', '0'],['A', 'B', 'D', '0', 'S', '0', '0', '0', '0', '0'],['A', 'B', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
compboard = [['A', 'B', 'D', 'P', 'S', '0', '0', '0', '0', '0'],['A', 'B', 'D', 'P', 'S', '0', '0', '0', '0', '0'],['A', 'B', 'D', '0', 'S', '0', '0', '0', '0', '0'],['A', 'B', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]

usersunken = []
compsunken = []
bombs = []


#Need a code that will search the board for a ship.
#If the ship is not there, then it is sunk
#However, we only want to be notified that the ship has been sunk once

#check = boat check

def lettersearch(x,b): #x is letter, b is board
    check = False #assume boat is not there
    for element in b: #check every space in the board
        if x in element: #if the letter in that place
            check = True #the boat is in the board
    return(check)

def usercheck():
    pcheck = lettersearch('P',userboard) #search the board for PT board
    if 'P' not in usersunken: #if P is not already indicated as underwater
        if pcheck == False: #if P is not there
            usersunken.append('P')
            print('The Computer sank your PT Boat!')

    scheck = lettersearch('S',userboard)
    if 'S' not in usersunken:
        if scheck == False:
            usersunken.append('S')
            print('The Computer sank your Submarine!')

    dcheck = lettersearch('D',userboard)
    if 'D' not in usersunken:
        if dcheck == False:
            usersunken.append('D')
            print('The Computer sank your Destroyer!')

    bcheck = lettersearch('B',userboard)
    if 'B' not in usersunken:
        if bcheck == False:
            usersunken.append('B')
            print('The Computer sank your Battleship!')

    acheck = lettersearch('A',userboard)
    if 'A' not in usersunken:
        if acheck == False:
            usersunken.append('A')
            print('The Computer sank your Aircraft Carrier!')

def compcheck():
    pcheck = lettersearch('P',compboard) 
    if 'P' not in compsunken: 
        if pcheck == False: 
            compsunken.append('P')
            usersink(shiptype('P'))

    scheck = lettersearch('S',compboard)
    if 'S' not in compsunken:
        if scheck == False:
            compsunken.append('S')
            usersink(shiptype('S'))

    dcheck = lettersearch('D',compboard)
    if 'D' not in compsunken:
        if dcheck == False:
            compsunken.append('D')
            usersink(shiptype('D'))

    bcheck = lettersearch('B',compboard)
    if 'B' not in compsunken:
        if bcheck == False:
            compsunken.append('B')
            usersink(shiptype('B'))

    acheck = lettersearch('A',compboard)
    if 'A' not in compsunken:
        if acheck == False:
            compsunken.append('A')
            usersink(shiptype('A'))



def comparelists(x): #x is your input list
    same = False #assume they do not contain the same elements
    x = set(x)
    y = set(['P','S','D','B','A'])
    if x==y: #if the elements in x are the same as the elements in y
        same = True
    return(same)

print(comparelists('P')) #should print false
print(comparelists(['B','D','A','S','P'])) #should print true
    
