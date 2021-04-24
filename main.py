#!/usr/bin/env python
# -*- coding:Utf8
from manager import Manager
from constantes import CATEGORIES_NAMES


manager=Manager()

manager.popular_categories()
manager.ten_products(CATEGORIES_NAMES)

