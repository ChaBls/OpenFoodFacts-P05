#!/usr/bin/env python
# -*- coding:Utf8
import mysql.connector


class ProductManager:
    
    def save(self, products):
        # The method allows the program to be connected to MariaDB database.

        data_base = mysql.connector.connect(host='localhost',user='chanelire',password='Baudelaire666!',database='OpenFoodFacts')
        cursor = data_base.cursor() # Allows to iterate through the database
        sql = "INSERT INTO product (name,nutriscore,url) VALUES (%s,%s,%s)"
        values = products
        cursor.execute(sql,values)
        data_base.commit()
        data_base.close()

