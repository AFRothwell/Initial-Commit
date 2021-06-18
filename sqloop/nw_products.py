# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:57:10 2021

@author: Andrew Rothwell
"""

import pyodbc

# Class to get information on any product 
class NwProducts:

    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursor = self.docker_Northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)
    
    def print_all_product_records(self):
        query_records = self._sql_query("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)
        

# x = NwProducts()
# x.print_all_product_records()

    def print_average_unit_price(self):
        query_records = self._sql_query("SELECT * FROM Products")
        
    # def print_sql_average(self):
    #     print(self._sql_query("SELECT AVG(UnitPrice) FROM Products".fetchall()))
        total_unit_price = []
        
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            total_unit_price.append(record.UnitPrice)
            
        print(sum(total_unit_price)/len(total_unit_price))
        

x = NwProducts()
x.print_average_unit_price()