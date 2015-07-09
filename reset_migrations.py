import os
import shutil

try:
  os.remove("db.sqlite3")
except(FileNotFoundError):
  pass

try:
  shutil.rmtree("annotation_app/migrations")
except(FileNotFoundError):
  pass

os.mkdir("annotation_app/migrations")
with open("annotation_app/migrations/__init__.py", 'a') as f:
  pass

os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
