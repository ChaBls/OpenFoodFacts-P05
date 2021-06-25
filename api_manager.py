#!/usr/bin/env python
# -*- coding:Utf8
from product import Product
from category import Category
from product_manager import ProductManager
import json
import requests


class APIManager:

    def popular_categories(self):
        # Categories objects are created from OpenFoodFacts API, saved and returned.

        category_request = requests.get('https://fr.openfoodfacts.org/categories.json') # request
        category_results = category_request.json()  # encoding
        category_list = category_results['tags']    # liste de dictionnaires
        sorted_category_list = sorted(category_list, key=lambda k:k['products'], reverse=True) # sorted list (by quantity of products)
        saved_categories=[]
        category_objects=[]
        for category in sorted_category_list[:1]: #changer en [:6]
            saved_categories.append(category['name'])
            category_objects.append(Category(name=category['name']))
        return saved_categories

    def ten_products(self,popular_categories):

        # Product objects are created using the previous method; objects are then returned.

        for category in self.popular_categories():
            product_request = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&json=1'.format(category))
            product_results = product_request.json()
            products_list = product_results['products'] # Liste de dictionnaires
            product_objects=[]
            for product in products_list[:10]: # Pour chaque dictionnaire de la liste
                product_objects.append(Product(name=product['product_name'],nutriscore=product['nutriscore_grade'],url=product['url'],categories=product['categories']))
            for product in product_objects:
                object_list = [product.name,product.nutriscore,product.url]
        return object_list

    def sending_products(self):
        # Product objects created in the previous method are saved; save() method from ProductManager class is called.

        ten_products_result = self.ten_products(self.popular_categories())
        product_manager=ProductManager()
        product_manager.save(ten_products_result)
        product_manager.saving_categories(ten_products_result)
    
