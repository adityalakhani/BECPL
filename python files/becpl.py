from tabulate import tabulate
import pymysql

#section - 1

def becpl():
    print("\n\t\tBHAGSONS ENGINEERS AND CONSULTANTS PVT. LTD.\n")
    print("1. For retriving records, press - 1\n")
    print("2. For reviewing attendance records and/or taking attendance , press - 2\n")
    print("3. For reviewing salary and deductions, press - 3\n")
    print("4. To quit, press - 4\n")

    choice = input("Enter valid option:")

    if choice == "1":                             #opens record section
        Rec()
        becpl()

    elif choice == "2":                           #opens attendance section
        attendanceRec()
        becpl()

    elif choice == "3":
        print("\nThis section is under progress.\n")
        becpl()

    elif choice == "4":                           #quits
        while True:
            break
    else:
        print("\nERROR! Invalid option entered, please try again.\n\n")
        becpl()

#section - 2

try:
    from becplFuncs import *
    file = open(r'password.txt', 'r')
    password = file.read()
    file.close()
    db = pymysql.connect(host = 'localhost', user = 'root', password = password)    #establishes connection
    c = db.cursor()                               #acivates cursor
    c.execute("use bhagsons")
    becpl()

except:
    print("Please run the setup before running the program.")
