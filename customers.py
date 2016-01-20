# -*- coding: UTF-8 -*-

import mysql.connector

class Customers():

    def __init__(self):
        self.CustomerID = ""
        self.CompanyName = ""
        self.ContactName = ""
        self.ContactTitle = ""
        self.Address = ""
        self.City = ""
        self.Region = ""
        self.PostalCode = ""
        self.Country = ""
        self.Phone = ""
        self.Fax = ""

    @staticmethod
    def parse(csv_row):
        a = Customers()
        if isinstance(csv_row,str):
            elemek = csv_row.split(";")
        else:
            elemek = csv_row
        a.CustomerID = elemek[0]
        a.CompanyName = elemek[1]
        a.ContactName = elemek[2]
        a.ContactTitle = elemek[3]
        a.Address = elemek[4]
        a.City = elemek[5]
        a.Region = elemek[6]
        a.PostalCode = elemek[7]
        a.Country = elemek[8]
        a.Phone = elemek[9]
        a.Fax = elemek[10]
        return a

    def persist(self):
        try:
            connection = mysql.connector.connect(user="root", password="r2e7d", host="127.0.0.1", port=3306, database='northwind')
            cursor = connection.cursor(buffered=True)
        except:
            print("Connection Error")
            return
        try:
            cursor.execute("INSERT INTO customers VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',\
                          '{10}')".format(self.CustomerID,
                                        self.CompanyName,
                                        self.ContactName,
                                        self.ContactTitle,
                                        self.Address,
                                        self.City,
                                        self.Region,
                                        self.PostalCode,
                                        self.Country,
                                        self.Phone,
                                        self.Fax))
        except Exception as e:
            print("Insertion Error: {}".format(e))
            connection.rollback()
            return
        connection.commit()
        connection.close()

    def __str__(self):
        result = self.CustomerID + "\t"
        result+=self.CompanyName + "\t"
        result+=self.ContactName + "\t"
        result+=self.ContactTitle + "\t"
        result+=self.Address + "\t"
        result+=self.City + "\t"
        result+=self.Region + "\t"
        result+=self.PostalCode + "\t"
        result+=self.Country + "\t"
        result+=self.Phone + "\t"
        result+=self.Fax + "\t"
        return result

    def to_csv(self):
        result = self.CustomerID + ";"
        result+=self.CompanyName + ";"
        result+=self.ContactName + ";"
        result+=self.ContactTitle + ";"
        result+=self.Address + ";"
        result+=self.City + ";"
        result+=self.Region + ";"
        result+=self.PostalCode + ";"
        result+=self.Country + ";"
        result+=self.Phone + ";"
        result+=self.Fax
        return result