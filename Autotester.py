# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:00:30 2015

@author: Deepti Boddapati
/deeptiboddapati
Automattically deletes database files, makes migrations and runs server.

"""
import manage
import os
import shutil
from random import sample

#figure out what code is being used to save bills now.
try:
    os.remove("db.sqlite3")
except(FileNotFoundError):
    pass

for i in os.listdir("annotation_app/migrations"):
    if i is not "__init__.py":
        try:
            shutil.rmtree("annotation_app/migrations/"+i,True)
        except(FileNotFoundError):
            pass
        try: 
            os.remove("annotation_app/migrations/"+i)
        except(FileNotFoundError):
            pass


os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
os.system("python manage.py runserver")
     
bill_nums = sample(range(1500),  30)

#put in code to generate 30 new bills when the migrations are made 
