#!/usr/bin/env python
# -*- coding:Utf8
from requests import api
from category import Category

class Product:
    def __init__(self,name,nutriscore,url,categories,id=None):
        self.id=id
        self.name=name
        self.nutriscore=nutriscore
        self.url=url
        self.categories=categories
        if type(categories) is str:
            self.generate_categories()

    def generate_categories(self):
        categories_list = self.categories.split(",")
        self.categories = [Category(x) for x in categories_list]

    def __str__(self):
        return self.name

