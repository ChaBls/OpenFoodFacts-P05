#!/usr/bin/env python
# -*- coding:Utf8
import mariadb
import sys

#Mariadb connection is established bellow
class Manager:

    def save(self):
        connection = mariadb.connect(
            user="chanelire",
            password=None,
            host="192.0.2.1",
            database="OpenFoodFacts"
        )

