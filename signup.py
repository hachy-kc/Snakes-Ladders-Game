def signup_function(username,password):     
    newfile = open("database.txt","a")      #opens the databasse file for appending
    newfile.write("New player\n")
    newfile.write(username+"\n")        #appends the users username and password for future logins
    newfile.write(password+"\n")
