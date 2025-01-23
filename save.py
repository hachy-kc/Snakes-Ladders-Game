def save_function(position):
    writer = open("savefile.txt","w")       #opens the savefile for writing
    writer.write(position+"\n")     #saves the position 