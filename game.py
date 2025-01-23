import random       #import random so as to randomize dice roll
import save         #import from save file

def loadgame(position):     #code for loading previous save
    class Node:
        def __init__(self,data):        #creating nodes for the linked list
            self.data = data
            self.next = None

    class Linked_list:
        def __init__(self,head):
            self.head = head

        def print_position(self,index):     #prints the position of the player on the board using the dice numbers rolled as the index
            curr = self.head
            count = 0
            while curr != None:
                if count == index:
                    return curr.data        #returns the data based on the index
                count += 1          #count increases by 1 while looping
                curr = curr.next

    A = Node("0")
    B = Node("1")
    C = Node("2")
    D = Node("3")
    E = Node("4")
    F = Node("5")
    G = Node("6")
    H = Node("7")
    I = Node("8")
    J = Node("9")
    K = Node("10")
    L = Node("11")
    M = Node("12")
    N = Node("13")
    O = Node("14")
    P = Node("15")
    Q = Node("16")
    R = Node("17")
    S = Node("18")
    T = Node("19")
    U = Node("20")
    V = Node("21")
    W = Node("22")
    X = Node("23")
    Y = Node("24")
    Z = Node("25")
    Ex = Node("26")
    Tr = Node("27")
    As = Node("28") 
    Dl = Node("29")
    Xd = Node("30")
    

    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    F.next = G
    G.next = H
    H.next = I
    I.next = J
    J.next = K
    K.next = L
    L.next = M
    M.next = N
    N.next = O
    O.next = P
    P.next = Q
    Q.next = R
    R.next = S
    S.next = T
    T.next = U
    U.next = V
    V.next = W
    W.next = X
    X.next = Y 
    Y.next = Z 
    Z.next = Ex 
    Ex.next = Tr 
    Tr.next = As 
    As.next = Dl
    Dl.next = Xd

    myboard = Linked_list(A)


    die_num = position      #position loaded from save is put on the board
    while int(myboard.print_position(die_num)) < 25:        #make the value an integer for inequality equation
        print("press enter when you want to roll the dice, type 'S' if you want to save")
        resp = input()
        if resp == "":      #pressing the enter key rolls the dice
            test = random.randint(1,6)      #gets a radnom integer between 1 and 6
            print("rolled", test)
            die_num += test
            new_pos = myboard.print_position(die_num)
            print("landed on",new_pos)

            if int(new_pos) == 10:      #if you land on 10 it moves you back 7 spaces to 3 and your new position is 3 and it will print snake 
                print("SNAKE")
                die_num = die_num - 7 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 17:
                print("SNAKE")
                die_num = die_num - 6 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 19:
                print("SNAKE")
                die_num = die_num - 7 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 8:
                print("SNAKE")
                die_num = die_num - 5 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 23:
                print("SNAKE")
                die_num = die_num - 10 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)


            if int(new_pos) == 2:       #if you land on 2 it moves you forward 4 spaces to 6 and your new position is 6 and it will print ladder
                print("LADDER")
                die_num = die_num + 4
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 9:
                print("LADDER")
                die_num = die_num + 7
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 18:
                print("LADDER")
                die_num = die_num + 2
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 22:
                print("LADDER")
                die_num = die_num + 2
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)


            if int(new_pos) == 25:
                print("CONGRATULATIONS")        #when player reaches 25 they win
                print("WINNER!!!")

            if int(new_pos) > 25:       #if player goes pass 25 they are not moved forward on the board 
                print("WENT PAST 25")
                die_num -= test
                print("land on 25 to WIN!!!")
                new_pos = myboard.print_position(die_num)
                print("current position:",new_pos)

        if resp == "S":
            print("saving will overwrite your previous save, do you wish to continue 'Y/N'")
            respon = input()
            if respon == "Y":               #pressing S will save and uses the imported save function to write the current position of the player
                position = new_pos
                save.save_function(position)
                print("GAME SAVED")
            if respon == "N":
                pass








def playgame ():        #code for a new game load
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    class Linked_list:
        def __init__(self,head):
            self.head = head

        def print_position(self,index):
            curr = self.head
            count = 0
            while curr != None:
                if count == index:
                    return curr.data 
                count += 1
                curr = curr.next

    A = Node("0")
    B = Node("1")
    C = Node("2")
    D = Node("3")
    E = Node("4")
    F = Node("5")
    G = Node("6")
    H = Node("7")
    I = Node("8")
    J = Node("9")
    K = Node("10")
    L = Node("11")
    M = Node("12")
    N = Node("13")
    O = Node("14")
    P = Node("15")
    Q = Node("16")
    R = Node("17")
    S = Node("18")
    T = Node("19")
    U = Node("20")
    V = Node("21")
    W = Node("22")
    X = Node("23")
    Y = Node("24")
    Z = Node("25")
    Ex = Node("26")
    Tr = Node("27")
    As = Node("28") 
    Dl = Node("29")
    Xd = Node("30")
    

    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    F.next = G
    G.next = H
    H.next = I
    I.next = J
    J.next = K
    K.next = L
    L.next = M
    M.next = N
    N.next = O
    O.next = P
    P.next = Q
    Q.next = R
    R.next = S
    S.next = T
    T.next = U
    U.next = V
    V.next = W
    W.next = X
    X.next = Y 
    Y.next = Z 
    Z.next = Ex 
    Ex.next = Tr 
    Tr.next = As 
    As.next = Dl
    Dl.next = Xd

    myboard = Linked_list(A)

    die_num = 0     #dice number will begin from 0 because player has not moved 
    while int(myboard.print_position(die_num)) < 25:
        print("press enter when you want to roll the dice, type 'S' if you want to save")
        resp = input()
        if resp == "": 
            test = random.randint(1,6)
            print("rolled", test)
            die_num += test
            new_pos = myboard.print_position(die_num)
            print("landed on",new_pos)

            if int(new_pos) == 10:
                print("SNAKE")
                die_num = die_num - 7 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 17:
                print("SNAKE")
                die_num = die_num - 6 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 19:
                print("SNAKE")
                die_num = die_num - 7 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 8:
                print("SNAKE")
                die_num = die_num - 5 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 23:
                print("SNAKE")
                die_num = die_num - 10 
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)


            if int(new_pos) == 2:
                print("LADDER")
                die_num = die_num + 4
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 9:
                print("LADDER")
                die_num = die_num + 7
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 18:
                print("LADDER")
                die_num = die_num + 2
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)
            if int(new_pos) == 22:
                print("LADDER")
                die_num = die_num + 2
                new_pos = myboard.print_position(die_num)
                print("new position:",new_pos)


            if int(new_pos) == 25:
                print("CONGRATULATIONS")
                print("WINNER!!!")

            if int(new_pos) > 25:
                print("WENT PAST 25")
                die_num -= test
                print("land on 25 to WIN!!!")
                new_pos = myboard.print_position(die_num)
                print("current position:",new_pos)

        if resp == "S":
            print("saving will overwrite your previous save, do you wish to continue 'Y/N'")
            respon = input()
            if respon == "Y":
                position = new_pos
                save.save_function(position)
                print("GAME SAVED")
            if respon == "N":
                pass

        
        





