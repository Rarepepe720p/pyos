import os
import platform

def getarg():
    arg = input()
    if arg == "dir":
        os.system("dir")
        getarg()
    elif arg == "cd":
        os.system("cd")
        getarg()
    elif "print" in arg:
        prst = input("Statement: ")
        print(prst)
        getarg()
    elif "echo" in arg:
        txtcont = input("File contents: ")
        file = open("userfile.txt","w")
        file.write(txtcont)
        file.close()
        getarg()
    elif arg == "write":
        file = open("userfile.txt","r")
        file.read()
        getarg()
    elif arg == "help":
        print("PyOS Help Center.\n")
        print("DIR: List contents of current directory.")
        print("CD: Display current directory.")
        print("PRINT: Print an integer, boolean, or string value to the console.")
        print("ECHO <filename> <extension>: Create a file with a specified extension. (Default is .txt)")
        print("READ: Print the contents of a file to the console.")
        getarg()
    elif arg == "ls -a":
        print("Processor: Intel(R) Core(TM)2 Duo CPU E8400 @ 3.00GHz, 3000 Mhz, 2 Core(s), 2 Log...")
        print("RAM: 4.00 GB")
        print("Memory: 3.90 GB")
        print("Available Virtual Memory: 1.78 GB")
        getarg()
    elif arg == "exit":
        os.system("exit")

print("Welcome to the PyOS. Type 'help' for help, or 'ls -a' for additional information.")
getarg()

