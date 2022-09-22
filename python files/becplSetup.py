import pymysql
import time

#section - 1

def connectivity():
    try:
        db = pymysql.connect(host = 'localhost', user = 'root', password = password)    #establishes connection
    except:
        print("\nIvalid password entered, please close and restart the setup.")
    c = db.cursor()
    print("\nLOADING, PLEASE WAIT.")
    try:
        c.execute("CREATE database bhagsons")
    except:
        print("\nDatabase bhagsons already exists.")
        while True:
            break
    c.execute("use bhagsons")
    try:
        c.execute("CREATE TABLE employee(eCode varchar(6) NOT NULL, name varchar(30) NOT NULL, fname varchar(30) NOT NULL, DOA date NOT NULL, DOJPF date NOT NULL, DOJESI date, designation varchar(20), UAN bigint(12) NOT NULL, pfNo varchar(12) NOT NULL, esicNo int(10), gender char(1) NOT NULL, DOB date NOT NULL, MOBno bigint(10) NOT NULL, PANno varchar(11), Aadharno bigint(12) NOT NULL, PRIMARY KEY(eCode, name))")
        c.execute("INSERT INTO employee VALUES('B001', 'Vinod Lakhani', 'L SH  Moolchand Lakhani', '1987-10-01', '1994-10-01 ', NULL, 'Director ',  100408378950, 'DL/16274/001', NULL, 'M ', '1967-01-21 ', 9350043139, 'AAFPL3717J ', 823878488972)")
        c.execute("INSERT INTO employee VALUES('B002', 'Sanjay Lakhani', 'L SH Moolchand Lakhani', '1987-10-01', '1994-10-01', NULL, 'Director', 100333613580, 'DL/16274/002', NULL, 'M', '1968-04-22', 9352200404, 'AABPL5677K', 918323207787)")
        c.execute("INSERT INTO employee VALUES('B003', 'Pramod Lakhani', 'L SH Moolchand Lakhani', '1994-10-01', '1994-10-01', NULL, 'Accountant', 100276845140, 'DL/16274/003', NULL, 'M', '1969-10-01', 9310043139, 'AAMPL4071A', 652669447203)")
        c.execute("INSERT INTO employee VALUES('B038', 'Ramjeet', 'SH Tribhuvan', '2008-04-24', '2008-04-24', '2008-04-24', 'Fitter', 100305914277, 'DL/16274/038', 1504798153, 'M', '1966-10-08', 7742513648, 'ANOPY2051N', 310189897295)")
        c.execute("INSERT INTO employee VALUES('B040', 'Jalaludeen', 'SH Rahimullah', '2009-12-18', '2009-12-18', '1975-09-15', 'Argon Welder', 100171869348, 'DL/16274/040', 1505063006, 'M', '1975-09-15', 8502813470, 'BBUPJ4810K', 394853663757)")
        c.execute("INSERT INTO employee VALUES('BECF46', 'Dalip Kumar', 'SH Jagdish', '2012-07-01', '2012-07-01', '2012-07-01', 'Helper', 100129422953, 'DL/16274/046', 1503961441, 'M', '1985-06-15', 8808950224, 'GBSPK4840M', 890703961835)")
        c.execute("INSERT INTO employee VALUES('BECF47', 'Kunwar Mohd', 'SH Mamura', '2012-07-12', '2012-07-12', '2012-07-12', 'Latheman', 100198956086, 'DL/16274/047', 1506853088, 'M', '1987-08-20', 7688921510, NULL, 439322144672)")
        c.execute("INSERT INTO employee VALUES('BECF48', 'Triloki', 'SH Ram Dhani', '2014-02-01', '2014-02-01', '2019-05-02', 'Polishman', 100012756447, 'DL/16274/048', 1507362793, 'M', '1968-11-15', 9950910875, 'AUUMPT5766E', 245399705079)")
        c.execute("INSERT INTO employee VALUES('BECF53', 'Ravindra', 'SH Jagdish', '2016-12-01', '2016-12-01', '2016-12-01', 'Argon Welder', 100311148946, 'DL/16274/053', 1505063007, 'M',  '1990-07-10', 9784435850, 'DACPR7455B', 800011630639)")
        c.execute("INSERT INTO employee VALUES('BECF54', 'Pappu', 'SH Ram Chandra', '2017-04-01', '2017-04-01', '2017-04-01', 'Fitter', 100267097172, 'DL/16274/054', 1503961443, 'M', '1980-04-26', 8003926090, 'DXAPP7262P', 954001875463)")
        c.execute("INSERT INTO employee VALUES('BECF55', 'Ranjeet Singh', 'SH Nemi Chand', '2018-03-01', '2018-03-01', '2018-03-01', 'Lath Operator', 101267926696, 'DL/16274/055', 1509430446, 'M', '1988-12-21', 9785551990, NULL, 676264320115)")
        c.execute("INSERT INTO employee VALUES('BECF56', 'Ram Ketar', 'SH Shiv Lal', '2018-03-01', '2018-03-01', '2018-03-01', 'Welder', 101267926704, 'DL/16274/056', 1509430425, 'M', '1976-01-01', 8400274321, 'CTGPR3762R', 896782752841)")
        c.execute("INSERT INTO employee VALUES('BECF57', 'Vishram Prajapat', 'SH Lala Ram Prajapat', '2018-05-01', '2018-05-01', '2018-05-01', 'Welder', 101301832160, 'DL/16274/057', 1507491628, 'M', '1979-07-15', 9660475313, NULL, 401130554256)")
        c.execute("INSERT INTO employee VALUES('BECF59', 'Harendra Kumar', 'SH Jagdeesh', '2018-08-01', '2018-08-01', '2018-08-01', 'Welder', 101347434979, 'DL/16274/059', 1509773095, 'M', '1998-07-07', 9116525113, 'HHVPK3248D', 832240845176)")
        c.execute("INSERT INTO employee VALUES('BECF60', 'Bindresh', 'L SH Khubani', '2018-08-01', '2018-08-01', '2018-08-01', 'Polishman', 100115028350, 'DL/16274/060', 1503968921, 'M', '1977-01-20', 7891988136, 'EEMPB7085C', 435566013892)")
    except:
        print("\nTable 'employee' and it's data already exists on your device!")
        while True:
            break
    try:
        c.execute("CREATE TABLE attendance(eCode varchar(6) NOT NULL, name varchar(30) NOT NULL, PRIMARY KEY(eCode, name))")
        c.execute("INSERT INTO attendance SELECT eCode, name from employee")
    except:
        print("\nTable 'attendance' and it's data already exists.")
        while True:
            break
    db.commit()
    print("\nINSTALLATION SUCCESSFUL!!")

#section - 2

passwd = open(r'password.txt', 'w+')
password = input("Enter the MySQL password of your device:")
try:
    passwd.write(password)
    connectivity()
except:
    while True:
        break
passwd.close()
time.sleep(3)