# -*- coding: UTF-8 -*-
import mysql.connector

class Employees():

    def __init__(self):
        self.EmployeeID = ""
        self.LastName = ""
        self.FirstName = ""
        self.Title = ""
        self.TitleOfCourtesy = ""
        self.BirthDate = ""
        self.HireDate = ""
        self.Address = ""
        self.City = ""
        self.Region = ""
        self.PostalCode = ""
        self.Country = ""
        self.HomePhone = ""
        self.Extension = ""
        self.Photo = ""
        self.Notes = ""
        self.ReportsTo = ""
        self.PhotoPath = ""
        self.Salary = ""


    @staticmethod
    def parse(csv_row):
        a = Employees()
        if isinstance(csv_row,str):
            elemek = csv_row.split(";")
        else:
            elemek = csv_row
        a.EmployeeID = elemek[0]
        a.LastName = elemek[1]
        a.FirstName = elemek[2]
        a.Title = elemek[3]
        a.TitleOfCourtesy = elemek[4]
        a.BirthDate = elemek[5]
        a.HireDate = elemek[6]
        a.Address = elemek[7]
        a.City = elemek[8]
        a.Region = elemek[9]
        a.PostalCode = elemek[10]
        a.Country = elemek[11]
        a.HomePhone = elemek[12]
        a.Extension = elemek[13]
        a.Photo = elemek[14]
        a.Notes = elemek[15]
        a.ReportsTo = elemek[16]
        a.PhotoPath = elemek[17]
        a.Salary = elemek[18]
        return a

    def persist(self):
        try:
            connection = mysql.connector.connect(user="root", password="r2e7d", host="127.0.0.1", port=3306, database='northwind')
            cursor = connection.cursor(buffered=True)
        except:
            print("Connection Error")
            return
        try:
            cursor.execute("INSERT INTO employees VALUES ({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}',\
                      '{11}','{12}','{13}',{14},'{15}',{16},'{17}',{18})".format(self.EmployeeID,
                                                                          self.LastName,
                                                                          self.FirstName,
                                                                          self.Title,
                                                                          self.TitleOfCourtesy,
                                                                          self.BirthDate,
                                                                          self.HireDate,
                                                                          self.Address,
                                                                          self.City,
                                                                          self.Region,
                                                                          self.PostalCode,
                                                                          self.Country,
                                                                          self.HomePhone,
                                                                          self.Extension,
                                                                          self.Photo,
                                                                          self.Notes,
                                                                          self.ReportsTo,
                                                                          self.PhotoPath,
                                                                          self.Salary))
        except Exception as e:
            print("Insertion Error: {}".format(e))
            connection.rollback()
            return
        connection.commit()
        connection.close()

    def __str__(self):
        result = self.EmployeeID + "\t"
        result+=self.LastName + "\t"
        result+=self.FirstName + "\t"
        result+=self.Title + "\t"
        result+=self.TitleOfCourtesy + "\t"
        result+=self.BirthDate + "\t"
        result+=self.HireDate + "\t"
        result+=self.Address + "\t"
        result+=self.City + "\t"
        result+=self.Region + "\t"
        result+=self.PostalCode + "\t"
        result+=self.Country + "\t"
        result+=self.HomePhone + "\t"
        result+=self.Extension + "\t"
        result+=self.Photo + "\t"
        result+=self.Notes + "\t"
        result+=self.ReportsTo + "\t"
        result+=self.PhotoPath + "\t"
        result+=self.Salary + "\t"
        return result

    def to_csv(self):
        result = self.EmployeeID + ";"
        result+=self.LastName + ";"
        result+=self.FirstName + ";"
        result+=self.Title + ";"
        result+=self.TitleOfCourtesy + ";"
        result+=self.BirthDate + ";"
        result+=self.HireDate + ";"
        result+=self.Address + ";"
        result+=self.City + ";"
        result+=self.Region + ";"
        result+=self.PostalCode + ";"
        result+=self.Country + ";"
        result+=self.HomePhone + ";"
        result+=self.Extension + ";"
        result+=self.Photo + ";"
        result+=self.Notes + ";"
        result+=self.ReportsTo + ";"
        result+=self.PhotoPath + ";"
        result+=self.Salary
        return result

