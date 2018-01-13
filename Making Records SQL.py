# Tables, Records with Database....

import MySQLdb as sql

con=sql.connect("127.0.0.1","root","ssviexe123","Records")
c=con.cursor()



def update_record():
    n=raw_input("Enter Name: ")
    p=raw_input("Enter Password: ")
    qry="update Info_record set Password= '%s' where Name= '%s' "%(p,n)
    r=c.execute(qry)
    if r>0:
        print "Record Updated"
    else:
        print "Error Occured! "
    con.commit()


def delete_record():
    n=raw_input("Enter Name: ")
    qry="delete from Info_record where Name= '%s' "%(n)
    r=c.execute(qry)
    if r:
        print "Record Deleted"
    else:
        print "Error"
    con.commit()


def login():
    n=raw_input("Enter Name: ")
    p=raw_input("Enter Password: ")
    qry="select Name,Password from Info_record where Name='%s' and Password='%s' "%(n,p)
    r=c.execute(qry)

    if r>0:
        print "Login Success"
    else:
        print "Login Failed"
    con.commit()


def show_table():
    qur="select * from Info_record"
    c.execute(qur)
    for data in c.fetchall():
        print data[0]+"\t"+data[1]+"\t"+data[2]+"\t"+data[3]
    con.commit()

def add_Record():
    n=raw_input("Enter Name:")
    p=raw_input("Enter Password: ")
    a=raw_input("Enter Address: ")
    e=raw_input("Enter Email ID: ")
    
    qry="insert into Info_record(Name, Password, Address, Email_Id)  values('%s','%s','%s','%s')" %(n,p,a,e)
    r=c.execute(qry)
    if r>0:
        print "Record Inserted"
    else:
        print "Error ! Try Again..."

    con.commit()


def intro():
    print "This is MySQL Database Entry Zone. \n Give appropriate Choices for the following : "
    print "Enter 1 for Login: \nEnter 2 for Adding New Record: \nEnter 3 for Updating Existing Records: \nEnter 4 for Deleting Records: \nEnter 5 for viewing the whole Table: "
    ch=input("Your Choice : ")
    if ch==1:
        login()
    elif ch==2:
        add_Record()
    elif ch==3:
        update_record()
    elif ch==4:
        delete_record()
    elif ch==5:
        show_table()
    else:
        print "Invalid Input"

    recall()    
def recall():
    x=input("Want to see the menu again? \nPress 1 for going to the menu... ")
    if x==1:
         intro()
    else:
        exit()

        
intro()


