def login_function(username,password):
    obj = open("database.txt","r")      #open database for reading
    line = obj.readline()           #read when line is not empty 
    while (line != ""):
        if line == username+"\n":       #read first line then verify 
            paswrd = obj.readline()     #read second line then verify
            if paswrd == password+"\n":     #if the saved username and password correlate with what was typed then return true
                return True
        line = obj.readline()

    return False