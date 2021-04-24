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
        self.products_objects=[]

    def popular_categories(self):
        category_request = requests.get('https://fr.openfoodfacts.org/categories.json') # request
        category_results = category_request.json()  # encoding
        category_list = category_results['tags']    # liste de dictionnaires
        sorted_category_list = sorted(category_list, key=lambda k:k['products'], reverse=True) # sorted list (by quantity of products)
        for category in sorted_category_list[:6]:
            self.saved_categories.append(category['name'])
            print(category['name'])

    def ten_products(self, CATEGORIES_NAMES):
        '''Chaque nom de catégorie est sauvegardé dans les constantes, dans la liste 'CATEGORIES_NAME'
        Dans une boucle 'for', pour chaque nom contenu dans cette liste:
        Une requête est faite à partir d'un URL, grâce au module 'requests'. Les accolades contenues dans le lien sont remplacées par le nom de la catégorie.
        La liste obtenue est encodée puis enregistrée dans la variable 'results'
        Dans une boucle 'for', pour chaque dictionnaire de la liste sauvegardée précédemment, un objet issu de la classe 'Product' est créé.
        Les attributs de ces objets sont obtenus à partir des paires clef/valeur du dictionnaire.
        '''
        for category in CATEGORIES_NAMES:
            request = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0= {} &json=1'.format(category))
            results = request.json()
            products_list = results['products'] # Liste de dictionnaires
            self.saved_products_list.append(products_list)  # Liste enregistrée dans la liste 'saved_products_list'
            for liste in self.saved_products_list: # Pour chaque liste dans la liste 'saved.products.list'
                for product in liste[:10]:  # Pour chaque dictionnaire de la liste 'products_list'
                    # Créer un objet Product()
                    self.products_objects.append(Product(id=product['id'],name=product['product_name'],nutriscore=product['nutriscore_grade'],url=product['url']))
                    # Afficher les ojects créés
                    print(self.products_objects)

                ''' Pour chaque objet dans la liste d'objets
                Afficher le nom
                Afficher l'id
                '''
                for objects in self.products_objects:
                    print(objects.name)
                    print(objects.id)

