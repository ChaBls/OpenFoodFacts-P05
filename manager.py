#!/usr/bin/env python
# -*- coding:Utf8
import json
import requests
from constantes import CATEGORIES_NAMES
from product import Product


class Manager:

    def __init__(self):
        self.saved_categories=[]
        self.saved_products_list=[]
        self.products_list=[]

    def popular_categories(self):
        category_request = requests.get('https://fr.openfoodfacts.org/categories.json') # request
        category_results = category_request.json()  # encoding
        category_list = category_results['tags']    # liste de dictionnaires
        sorted_category_list = sorted(category_list, key=lambda k:k['products'], reverse=True) # sorted list (by quantity of products)
        for category in sorted_category_list[:6]:
            self.saved_categories.append(category['name'])
            print(category['name'])

    def ten_products(self, CATEGORIES_NAMES):
        for category in CATEGORIES_NAMES:
            request = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0= {} &json=1'.format(category))
            results = request.json()
            products_list = results['products'] # liste de dictionnaires
            self.saved_products_list.append(products_list)
            for liste in self.saved_products_list:
                for product in liste[:10]:
                    self.products_list.append(Product(id=product['id'],name=product['product_name'],nutriscore=product['nutriscore_grade'],url=product['url']))
                    
                for objects in self.products_list:
                    print(objects.name)
                    print(objects.id)

