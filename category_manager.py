#!/usr/bin/env python
# -*- coding:Utf8
import mysql.connector


class CategoryManager:
    
    def save(self,products):
        data_base = mysql.connector.connect(host='localhost',user='chanelire',password='Baudelaire666!',database='OpenFoodFacts')
        cursor = data_base.cursor()
        sql = "INSERT INTO category (name) VALUES (%s)"
        values = products
        cursor.execute(sql,values)
        data_base.commit()
        sql_dinstinct = "INSERT DISTINCT name FROM categories"
        cursor.execute(sql_dinstinct)
        print(cursor.lastrowid) # Test
        data_base.close()

