import pickle
import threading
import serial

serialcomm = serial.Serial('COM6', 9600)
serialcomm.timeout = 1

pain = 0
oldOpen = 0

# Open the file in binary mode

def printits():
    threading.Timer(5, printits).start()
    global pain
    global oldOpen
    with open('file.pkl', 'rb') as test:
        # Call load method to deserialze
        mvtmp = pickle.load(test)

    if mvtmp == 0:
        myvar = "zero"
    else:
        myvar = str(mvtmp)

    pain = pain + 1

    if oldOpen != myvar:
        serialcomm.write(myvar.encode())
        print(myvar)
        # time.sleep(1)
        print(serialcomm.readline().decode('ascii'))
        print("runtime = " + str((pain * 5) / 60) + " minutes")
        print("empty spaces =" + myvar)
        oldOpen = myvar

printits()
