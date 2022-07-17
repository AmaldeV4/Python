from datetime import datetime


now = datetime.now()
dt = now.strftime('%d/%m/%y %H:%M:%S')


def logger():
    f = open("file.txt", "a")
    f.write("\n" + user + " logged at " + dt)
    f.close()


while True:
    user = input("Enter Username: ")
    if type(user) == str:
        print("Hello " + user + "! You have been logged in")
        logger()
        break
    elif type(user) == int or float:
        print("Only letters are allowed!")
