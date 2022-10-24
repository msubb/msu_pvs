import pickle
import threading
import github.InputFileContent
from github import Github
# import serial

# serialcomm = serial.Serial('COM6', 9600)
# serialcomm.timeout = 1

pain = 0
oldOpen = 0


# Open the file in binary mode

def printit():
    threading.Timer(5, printit).start()
    global pain
    global oldOpen
    with open('file.pkl', 'rb') as test:
        # Call load method to deserialze
        myvar = pickle.load(test)
    pain = pain + 1

    if oldOpen != myvar:
        g = Github("secret")

        gist = g.get_gist("004e205c856d5f934704333f5725d61e")
        gist.edit(
            "",
            {"gistfile1.txt": github.InputFileContent(str(myvar))},
        )

        print("runtime = " + str((pain * 5) / 60) + " minutes")
        print("empty spaces =" + str(myvar))

        # i = myvar.strip()
        #
        # serialcomm.write(i.encode())
        #
        # time.sleep(0.5)
        #
        # print(serialcomm.readline().decode('ascii'))

        oldOpen = myvar

# def serial():
#     serialcomm.write(i.encode())
#
#     time.sleep(0.5)
#
#     print(serialcomm.readline().decode('ascii'))
#
# serialcomm.close()

printit()
