import json
json_data=[{'name':"Dhivya",'age':21,'Permanent_staff':True,'salary':75000.00,'dept_desgn':'Developer'},
     {'name':"Renu",'age':35,'Permanent_staff':False,'salary':56000.00,'dept_desgn':"ML Engineer"},
     {'name':"Manu",'age':34,'Permanent_staff':True,'salary':78000.00,'dept_desgn':'Web Designer'},
     {'name':"Shardha",'age':23,'Permanent_staff':True,'salary':45000.00,'dept_desgn':'Data Scientist'},
     {'name':"Kumar",'age':21,'Permanent_staff':True,'salary':67000.00,'dept_desgn':'Manager'}]

res=json.dumps(json_data)
import mysql.connector
mydb = mysql.connector.connect(host="localhost",username="root",password="Dharani@379")
print(mydb)
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)


mydb = mysql.connector.connect(host="localhost",username="root",password="Dharani@379",database="jsonrecords2")
dbse = mydb.cursor()
dbse.execute("CREATE TABLE employee (name VARCHAR(255),age INT, permanent_staff VARCHAR(255), salary DOUBLE, dept_and_designation VARCHAR(255))")
dbse =mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)

dbse = mydb.cursor()
dbse.execute("SHOW COLUMNS FROM employee")
for value in dbse:
    print(value)

dbse = mydb.cursor()
sql = "INSERT INTO employee (name ,age, permanent_staff,salary,dept_designation) VALUES (%(name)s,%(age)s,%(permanent_staff)s,%(salary)s,%(dept_designation)s)"
for i in res:
    dbse.execute(sql,i)
    
mydb.commit()
dbse.close()
mydb.close()


