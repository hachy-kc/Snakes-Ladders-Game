import signup           #import from signup file                 
import login            #import from login file
import game         #import from game file

status = False
print("HACHI'S SNAKES & LADDERS, Are you new? Y/N")
ans = input()
if ans == "Y":          
    print("enter a username")       #enter the username you wish to use and password
    user = input()
    print("enter a password")
    password = input()
    signup.signup_function(user,password)           #uses the sign up function imported to document your credentials
    status = True

    pass

if ans == "N":
    print("OKAY! enter your username")
    user = input()      #enter your user name and password so they can be verified by the login function that is imported
    print("password")
    password = input()
    if login.login_function(user,password) == True:     #if the credentials match the documented credentials then status is true
        print("welcome player")
        status = True
    else:
        print("username or password incorrect, please try again")       #if the credentials are incorrect this message will print and you wont be allowed to proceed further because status is FALSE
        status = False
    pass


if status == True:
    print("would you like to load a previous game or start new one? (respond with 'load' or 'new')")
    ans = input()
    if ans == "load":
        obj = open("savefile.txt","r")
        line = obj.readline()
        while line != "":
            break
        print("loading game...")
        print("game loaded")
        print("currently at position", line)        #if asked to load it will load previous savefile and read the line to get your position 
        posit = int(line)       #converts the string data that was read to and integer 
        game.loadgame(posit)
        pass
    if ans == "new":
            game.playgame()     #if you type new game it will proceed to play game from beginning without overwriting previous save
            pass
