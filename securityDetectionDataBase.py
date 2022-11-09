import sqlite3
db=sqlite3.connect("securityDetection.db")
cursor=db.cursor()
# def createTables():
#     tableList=["Employee", "people_data"]
#     for table in tableList:
#         cursor.execute(f"create table if not exists '{table}'(ssn integer ,fName text,lName text,address text ,phone integer)")
#
#     cursor.execute("create table if not exists criminal(cssn integer pk,fName text,lName text,address text ,weaponType text)")
#     cursor.execute("create table if not exists AllowedToHaveWeapon(ssn integer pk,weaponType text)")
#     db.commit()
#     db.close()
#
# createTables()

# def insertdata():
    # cursor.execute("insert into Employee(ssn ,fName ,lName,address ,phone) values(01, 'Dr_Wael', 'Zakria', '2 ainShams st' ,01245)")
    # cursor.execute("insert into Employee(ssn ,fName ,lName,address ,phone) values(02, 'glgl', 'Ahmed', '2 Azba st' ,05445)")
    # cursor.execute("insert into Employee(ssn ,fName ,lName,address ,phone) values(03, 'Ahmed', 'Salem', '2 Shoubra st' ,32145)")
    # cursor.execute("insert into Employee(ssn ,fName ,lName,address ,phone) values(04, 'yousef', 'masoud', '2 moqtm st' ,65487)")
    # cursor.execute("insert into Employee(ssn ,fName ,lName,address ,phone) values(05, 'mohamed', 'madhat', '2 ShoubraEgy st' ,85214)")

    # cursor.execute("insert into AllowedToHaveWeapon(ssn ,weaponType) values(01, 'knife')")
    # cursor.execute("insert into AllowedToHaveWeapon(ssn ,weaponType) values(03, 'gun')")
    # db.commit()

# insertdata()

# cursor.execute("select  e.ssn,fName,weaponType from Employee as e , AllowedToHaveWeapon as a where e.ssn=a.ssn ")
# print(cursor.fetchall())