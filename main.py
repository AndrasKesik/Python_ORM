# -*- coding: UTF-8 -*-
import os
import mysql.connector
import datetime
from employees import Employees
import decimal
from customers import Customers
from orders import Orders
from orderdetails import Orderdetails
clear = lambda: os.system('cls')

EMPLOYEES_CSV = "csv/employees.csv"
CUSTOMERS_CSV = "csv/customers.csv"
ORDERS_CSV = "csv/orders.csv"
ORDERDETAILS_CSV = "csv/order_details.csv"

EMPLOYEES_HEAD = "EmployeeID;LastName;FirstName;Title;TitleOfCourtesy;BirthDate;HireDate;Address;City;Region;PostalCode;Country;HomePhone;Extension;Photo;Notes;ReportsTo;PhotoPath;Salary"
CUSTOMERS_HEAD = "CustomerID;CompanyName;ContactName;ContactTitle;Address;City;Region;PostalCode;Country;Phone;Fax"
ORDERS_HEAD = "OrderID;CustomerID;EmployeeID;OrderDate;RequiredDate;ShippedDate;ShipVia;Freight;ShipName;ShipAddress;ShipCity;ShipRegion;ShipPostalCode;ShipCountry"
ORDERDETAILS_HEAD = "OrderID;ProductID;UnitPrice;Quantity;Discount"



def csv_reader(file,osztaly):
    with open(file, "r", encoding="utf-8") as f:
        csv_data = f.read().split("\n")
    del(csv_data[0])

    obj_lista = []
    for i in range(len(csv_data)):
        if len(csv_data[i]) > 0:
            obj_lista.append(osztaly.parse(csv_data[i]))
    return obj_lista

def db_reader(tabla):
    try:
        connection = mysql.connector.connect(user="root", password="r2e7d", host="127.0.0.1", port=3306, database='northwind')
        cursor = connection.cursor(buffered=True)
    except Exception as e:
        print("Connection Error: ".format(e))

    cursor.execute("SELECT * FROM {}".format(tabla))
    data = cursor.fetchall()
    return data

def csv_writer(file,honnan,head):
    with open(file, "w", encoding="utf-8") as f:
        f.write(head+"\n")
        for i in honnan:
            f.write(i.to_csv()+"\n")

def row_normalizer(data_row):
    normalized = []
    for i in data_row:
        if i == None:
            normalized.append("NULL")
        elif isinstance(i,datetime.datetime):
            sztringdate = datetime.datetime.strftime(i, "%Y-%m-%d")
            normalized.append(sztringdate)
        elif isinstance(i, int) or isinstance(i, float) or isinstance(i, decimal.Decimal):
            normalized.append(str(i))
        elif isinstance(i, bytes):
            normalized.append("NULL")        # i.decode(utf-8)  // PICTURE DECODING DOESN'T WORK YET
        else:
            normalized.append(i)
    return normalized

def table_normalizer(tabla):
    normalized_tabla= []
    data = db_reader(tabla)
    for i in data:
        normalized_tabla.append(row_normalizer(i))
    return normalized_tabla

def to_obj(ntable,osztaly):
    obj_list = []
    for i in ntable:
        obj_list.append(osztaly.parse2(i))
    return obj_list

def from_csv_to_db(csv_file,osztaly):
    lista = csv_reader(csv_file, osztaly)
    for i in lista:
        i.persist()


# CSV TO DB WORKING WITH CORRECT CSV DATA
"""
from_csv_to_db(EMPLOYEES_CSV, Employees)
from_csv_to_db(CUSTOMERS_CSV, Customers)
from_csv_to_db(ORDERS_CSV, Orders)
from_csv_to_db(ORDERDETAILS_CSV, Orderdetails)
"""

run = 1
while(run):
    clear()
    user_input=input("Melyik tablabol szeretnel csv-t csinálni?:"
          "\n(1) Employees"
          "\n(2) Customers"
          "\n(3) Orders"
          "\n(4) Orderdetails"
          "\n(5) EXIT "
          "\n> ")

    if user_input == "1":
        employees = to_obj(table_normalizer("employees"),Employees)
        csv_writer("employees_from_db.csv",employees,EMPLOYEES_HEAD)
    elif user_input == "2":
        customers = to_obj(table_normalizer("customers"),Customers)
        csv_writer("customers_from_db.csv",customers,CUSTOMERS_HEAD)
    elif user_input == "3":
        orders = to_obj(table_normalizer("orders"),Orders)
        csv_writer("orders_from_db.csv",orders,ORDERS_HEAD)
    elif user_input == "4":
        orderdetails = to_obj(table_normalizer("orderdetails"),Orderdetails)
        csv_writer("orderdetails_from_db.csv",orderdetails,ORDERDETAILS_HEAD)
    elif user_input == "5":
        run = 0
