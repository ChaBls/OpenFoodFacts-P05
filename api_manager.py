#!/usr/bin/env python
# -*- coding:Utf8
from product import Product
from category import Category
from product_manager import ProductManager
import json
import requests


class APIManager:

    def popular_categories(self):
        '''A request is made with "requests" module, the result is encoded and saved into "category_results".
        "tags" list (from the results) is saved into "category_list" and contains a dictionaries list.
        The list is sorted and saved into "sorted_category_list" and 2 empty lists are created : saved_categories" and "category_objects".
        Categories names are saved into the dirst empty list and Category() objects are created and saved, with the previously saved names as "name" attributes.
        The method returns categories names.
        '''
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
        '''Each category name is saved into "saved_categories" list, created in the previous method.
        In the following "for" loop, for each dictionary contained in "saved_categories":
        A request is done from an URL, with the "requests" module. Each "{}" in the link is replaced by the name of the category.
        The final list is encoded and saved into "results".
        Dictionary list, coming from the request, is saved into "products_list".
        In "for" loop, for each dictionary of "products_list", a Product() object is created and saved into "product_objects" list.
        The attributes of these objects are obtained from dictionaries key/value.
        The method returns a list of Product() objects.
        '''
        for category in self.popular_categories():
            product_request = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&json=1'.format(category))
            product_results = product_request.json()
            products_list = product_results['products'] # Liste de dictionnaires
            product_objects=[]
            for product in products_list[:10]: # Pour chaque dictionnaire de la liste
                product_objects.append(Product(name=product['product_name'],nutriscore=product['nutriscore_grade'],url=product['url']))
            return product_objects

    def sending_products(self, ten_products):
        product_manager=ProductManager()
        product_manager.save()

