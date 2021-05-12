#!/usr/bin/env python
# -*- coding:Utf8
from category_manager import CategoryManager
from product_manager import ProductManager
from api_manager import APIManager


manager_object=APIManager()

# We ask the program to create 10 objects from Product(), based on the categories we've saved with the 1st method.
manager_object.sending_products(manager_object.ten_products(manager_object.popular_categories()))

