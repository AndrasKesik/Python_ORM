# -*- coding: UTF-8 -*-
import mysql.connector
class Orders():

    def __init__(self):
        self.OrderID = ""
        self.CustomerID = ""
        self.EmployeeID = ""
        self.ContactTitle = ""
        self.OrderDate = ""
        self.RequiredDate = ""
        self.ShippedDate = ""
        self.ShipVia = ""
        self.Freight = ""
        self.ShipName = ""
        self.ShipAddress = ""
        self.ShipCity = ""
        self.ShipRegion = ""
        self.ShipPostalCode = ""
        self.ShipCountry = ""

    @staticmethod
    def parse(csv_row):
        a = Orders()
        elemek = csv_row.split(";")
        a.OrderID = elemek[0]
        a.CustomerID = elemek[1]
        a.EmployeeID = elemek[2]
        a.ContactTitle = elemek[3]
        a.OrderDate = elemek[4]
        a.RequiredDate = elemek[5]
        a.ShippedDate = elemek[6]
        a.ShipVia = elemek[7]
        a.Freight = elemek[8]
        a.ShipName = elemek[9]
        a.ShipAddress = elemek[10]
        a.ShipCity = elemek[11]
        a.ShipRegion = elemek[12]
        a.ShipPostalCode = elemek[13]
        a.ShipCountry = elemek[14]
        return a

    @staticmethod
    def parse2(elemek):
        a = Orders()
        a.OrderID = elemek[0]
        a.CustomerID = elemek[1]
        a.EmployeeID = elemek[2]
        a.OrderDate = elemek[3]
        a.RequiredDate = elemek[4]
        a.ShippedDate = elemek[5]
        a.ShipVia = elemek[6]
        a.Freight = elemek[7]
        a.ShipName = elemek[8]
        a.ShipAddress = elemek[9]
        a.ShipCity = elemek[10]
        a.ShipRegion = elemek[11]
        a.ShipPostalCode = elemek[12]
        a.ShipCountry = elemek[13]
        return a

    def persist(self):
        try:
            connection = mysql.connector.connect(user="root", password="r2e7d", host="127.0.0.1", port=3306, database='northwind')
            cursor = connection.cursor(buffered=True)
        except:
            print("Connection Error")
            return
        try:
            cursor.execute("INSERT INTO employees VALUES ({0},'{1}',{2},'{3}','{4}','{5}',{6},{7},'{8}','{9}','{10}',\
                      '{11}','{12}','{13}')".format(self.OrderID,
                                                    self.CustomerID,
                                                    self.EmployeeID,
                                                    self.OrderDate,
                                                    self.RequiredDate,
                                                    self.ShippedDate,
                                                    self.ShipVia,
                                                    self.Freight,
                                                    self.ShipName,
                                                    self.ShipAddress,
                                                    self.ShipCity,
                                                    self.ShipRegion,
                                                    self.ShipPostalCode,
                                                    self.ShipCountry))
        except Exception as e:
            print("Insertion Error: {}".format(e))
            connection.rollback()
            return
        connection.commit()
        connection.close()

    def __str__(self):
        result = self.OrderID + "\t"
        result+=self.CustomerID + "\t"
        result+=self.EmployeeID + "\t"
        result+=self.OrderDate + "\t"
        result+=self.RequiredDate + "\t"
        result+=self.ShippedDate + "\t"
        result+=self.ShipVia + "\t"
        result+=self.Freight + "\t"
        result+=self.ShipName + "\t"
        result+=self.ShipAddress + "\t"
        result+=self.ShipCity + "\t"
        result+=self.ShipRegion + "\t"
        result+=self.ShipPostalCode + "\t"
        result+=self.ShipCountry + "\t"
        return result

    def to_csv(self):
        result = self.OrderID + ";"
        result+=self.CustomerID + ";"
        result+=self.EmployeeID + ";"
        result+=self.OrderDate + ";"
        result+=self.RequiredDate + ";"
        result+=self.ShippedDate + ";"
        result+=self.ShipVia + ";"
        result+=self.Freight + ";"
        result+=self.ShipName + ";"
        result+=self.ShipAddress + ";"
        result+=self.ShipCity + ";"
        result+=self.ShipRegion + ";"
        result+=self.ShipPostalCode + ";"
        result+=self.ShipCountry

        return result