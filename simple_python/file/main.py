user = input("You want to access the python file[y/n]: ")
print("\n")
if user =="y" or "Y" :
    f = open("pythonfile.txt", "w")
    print(f.read())
    f.close()
elif user == "n" :
    print("You exited successfully")
    exit()
else:
    print("You exited")
