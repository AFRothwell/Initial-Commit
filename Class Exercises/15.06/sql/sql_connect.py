# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:12:25 2021

@author: Andrew Rothwell
"""

import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()


cursor.execute("SELECT @@version;")
row = cursor.fetchone()


# cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(cust_rows)


rows = cursor.execute("SELECT * FROM Products").fetchall()

# for record in rows:
#     print(record.UnitPrice)

 
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)