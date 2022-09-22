from tabulate import tabulate
import pymysql

#section - 1

file = open(r'password.txt', 'r')
password = file.read()
file.close
try:
    db = pymysql.connect(host = 'localhost', user = 'root', password = password)    #establishes connection
    c = db.cursor()                               #acivates cursor
    c.execute("use bhagsons")

except:
    print("\n")


#section - 2

def showAllRec():                             #fetches records of all
    c.execute("select * from employee")
    rows = c.fetchall()
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    for tup in rows:
        lst = list(tup)
        data.append(lst)
    print(tabulate(data))

def singleRecviaEcode():
    eCode = input("\nEnter Employee Code:")                             #takes employee code
    c.execute("Select * from employee WHERE eCode = '"+eCode.upper()+"'")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to display table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee with Employee Code",eCode,"found.")
        print("\n")
        singleRecEcode()

def singleRecviaName():
    name = input("\nEnter name of employee:")                           #takes name of employee
    c.execute("Select * from employee WHERE name LIKE '%"+name.capitalize()+"%'")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to display table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee named",name,"found.")
        print("\n")
        singleRecviaName()

def singleRecviaMobNo():
    mob = input("\nEnter employee's mobile number:")                    #takes mobile number of employee
    c.execute("Select * from employee where MOBno = "+mob+"")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to display table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employe with mobile number",mob,"found.")
        singleRecviaMobNo()

def singleRecviaPANno():
    pan_no = input("\nEnter employee's PAN number:")                    #takes PAN number of employee
    c.execute("SELECT * from employee WHERE PANno = '"+pan_no.upper().strip()+"'")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to display table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee with PAN no",pan_no,"found.")
        singleRecviaPANno()

def singleRecviaAadhar():
    a_no = input("\nEnter employee's Aadhar number:")                   #takes Aadhar number of employee
    c.execute("Select * from employee WHERE Aadharno = "+a_no+"")
    row = c.fetchmany(1)
    data = [["ECode", "Name", "Father's Name", "DOA", "DOJ PF", "DOJ ESI", "Designation", "UAN", "PF no", "ESIC no", "Gender", "DOB", "MOB no", "PAN no", "Aadhar no"]]
    while row:                                                          #parses row
        for tup in row:
            lst = list(tup)                                             #converts tuple to list
            data.append(lst)                                            #adds data to display table 
        print(tabulate(data))
        break
    else:                                                               #error statement
        print("\nNo employee with Aadhar number",a_no,"found.")
        print("\n")
        singleRecviaAadhar()

def Rec():
    print("\n\t\t\tEMPLOYEE DATA")
    print("\n1. For retriving information of all employees, press - 1\n")
    print("2. For retriving information based on employee's code, press - 2\n")
    print("3. For retriving information based on Name, press - 3\n")
    print("4. For retriving information based on mobile number, press - 4\n")
    print("5. For retriving information based on Pan number, press - 5\n")
    print("6. For retriving information based on Aadhar number, press - 6\n")

    info = input("Enter valid option:")

    if info == "1":
        print("\n\t\t\t\t\t\tEMPLOYEE INFO\n")
        showAllRec()

    elif info == "2":
        singleRecviaEcode()

    elif info == "3":
        singleRecviaName()

    elif info == "4":
        singleRecviaMobNo()

    elif info == "5":
        singleRecviaPANno()

    elif info == "6":
        singleRecviaAadhar()


#section - 2

def attendance():
    c.execute("select eCode, name from attendance ORDER BY name")
    rows = c.fetchall()
    day = input("Enter the date:")
    month = input("Enter the month:")
    year = input("Enter the year:")                                     #takes current date
    date = day+'_'+month.title()+'_'+year
    print("\n")
    try:
        c.execute("ALTER TABLE attendance ADD "+date+" char(2) NOT NULL")   #creates new column of input date
        db.commit()
        for r in rows:
            print(r[0] + " "*((12- len(r[0])))+ "|" + " "*(8) + r[1] + " "*((18- len(r[1]))), end = '')
            status = input(":") #takes attendance status (present, absent, casual leave, paid leave, sick leave)
            print('\n')
            if status.upper() == "P":
                c.execute("UPDATE attendance SET "+date+" ='P' WHERE eCode = '"+r[0]+"'")   #updates status present
                db.commit()
            elif status.upper() == "A":
                c.execute("UPDATE attendance SET "+date+" ='A' WHERE eCode = '"+r[0]+"'")   #updates status absent
                db.commit()
            elif status.upper() == "CL":
                c.execute("UPDATE attendance SET "+date+" ='CL' WHERE eCode = '"+r[0]+"'")  #updates status casual leave
                db.commit()
            elif status.upper() == "EL":
                c.execute("UPDATE attendance SET "+date+" ='EL' WHERE eCode = '"+r[0]+"'")  #updates status paid leave
                db.commit()
            elif status.upper() == "SL":
                c.execute("UPDATE attendance SET "+date+" ='SL' WHERE eCode = '"+r[0]+"'")  #updates status sick leave
                db.commit()
            else:
                print("\nERROR! Invalid Entry, please start over.\n")
                c.execute("Alter table attendance drop "+date+"")
                db.commit()
                attendance()
    except:
        print("The attendance of",date,"either already exists or is invalid.")
        attendance()

def retriveAttendanceMonth():
    month = input("Enter month:")
    print("\n")
    if month  == "sept":
        c.execute("Select eCode, name, 04sept20, 05sept20, 06sept20, 07sept20, 08sept20, 09sept20, 10sept20, 11sept20, 12sept20, 13sept20, 14sept20, 15sept20, 16sept20, 17sept20, 18sept20, 19sept20, 20sept20, 21sept20, 22sept20, 23sept20, 24sept20, 25sept20, 26sept20, 27sept20, 28sept20, 29sept20, 30sept20 from attendance ORDER BY name")
        row = c.fetchall()
        data = [['', '', '4th', '5th', '6th', '7th']]
        for tup in row:
            lst = list(tup)
            data.append(lst)
        print(tabulate(data))

def retriveAttendanceDate():
    day = input("Enter the date:")
    month = input("Enter the month:")
    year = input("Enter the year:")
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if (month.title() in months) and 1 < int(day) < 30 and int(year):
        date = day+'_'+month.title()+'_'+year
        print("\n")
        data1 = ['', '']
        data1.append(date)
        try:
            c.execute("Select eCode, name, "+date+" from attendance ORDER BY name")
            row = c.fetchall()
            data = []
            data.append(data1)
            for tup in row:
                lst = list(tup)
                data.append(lst)
            print(tabulate(data))
        except:
            print("Attendance of date '"+day+" "+month+" "+year+"' does not exist.")

    else:
        print("\nInvalid date entered, please try again.")

def deleteAttendanceRecDate():
    day = input("Enter the date:")
    month = input("Enter the month:")
    year = input("Enter the year:")
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if (month.title() in months) and int(day) and int(year):
        date = str(day)+'_'+month.title()+'_'+year
        c.execute("Alter table attendance drop "+date+"")
        db.commit()
        print("\nRecord successfully deleted.\n")

    else:
        print("\nInvalid date entered, please enter again.\n")
        deleteAttendanceRecDate()

def attendanceRec():
    print("\n\t\tATTENDANCE\n")
    print("1. For taking attendance, press - 1\n")
    print("2. For reviewing attendance(monthly), press - 2\n")
    print("3. For reviewing attendance(daily), press - 3\n")
    print("4. For delete attendance record, press - 4\n")

    choice = input("Enter valid option:")
    print("\n")
    if choice == "1":
        attendance()

    elif choice == "2":
        print("This section is under progress.")

    elif choice == "3":
        retriveAttendanceDate()

    elif choice == "4":
        deleteAttendanceRecDate()