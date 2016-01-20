# -*- coding: UTF-8 -*-
import mysql.connector

class Orderdetails():

    def __init__(self):
        self.OrderID = ""
        self.ProductID = ""
        self.UnitPrice = ""
        self.Quantity = ""
        self.Discount = ""

    @staticmethod
    def parse(csv_row):
        a = Orderdetails()
        elemek = csv_row.split(";")
        a.OrderID = elemek[0]
        a.ProductID = elemek[1]
        a.UnitPrice = elemek[2]
        a.Quantity = elemek[3]
        a.Discount = elemek[4]
        return a

    @staticmethod
    def parse2(elemek):
        a = Orderdetails()
        a.OrderID = elemek[0]
        a.ProductID = elemek[1]
        a.UnitPrice = elemek[2]
        a.Quantity = elemek[3]
        a.Discount = elemek[4]
        return a

    def persist(self):
        try:
            connection = mysql.connector.connect(user="root", password="r2e7d", host="127.0.0.1", port=3306, database='northwind')
            cursor = connection.cursor(buffered=True)
        except:
            print("Connection Error")
            return
        try:
            cursor.execute("INSERT INTO orderdetails VALUES ({0},{1},{2},{3}, \
                          {4})".format(self.OrderID,
                                        self.ProductID,
                                        self.UnitPrice,
                                        self.Quantity,
                                        self.Discount))
        except Exception as e:
            print("Insertion Error: {}".format(e))
            connection.rollback()
            return
        connection.commit()
        connection.close()

    def __str__(self):
        result = self.OrderID + "\t"
        result+=self.ProductID + "\t"
        result+=self.UnitPrice + "\t"
        result+=self.Quantity + "\t"
        result+=self.Discount + "\t"
        return result

    def to_csv(self):
        result = self.OrderID + ";"
        result+=self.ProductID + ";"
        result+=self.UnitPrice + ";"
        result+=self.Quantity + ";"
        result+=self.Discount
        return result