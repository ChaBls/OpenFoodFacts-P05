#!/usr/bin/env python
# -*- coding:Utf8
import mysql.connector


class ProductManager:
    
    def save(self, products):
        # The method allows the program to be connected to MariaDB database.

        for product in products:
            data_base = mysql.connector.connect(host='localhost',user='chanelire',password='Baudelaire666!',database='OpenFoodFacts')
            cursor = data_base.cursor() # Allows to iterate through the database
            cursor.execute("INSERT INTO products(name,nutriscore,url) VALUES (product.name,product.nutriscore,product.url")
            data_base.commit()
            data_base.close()

