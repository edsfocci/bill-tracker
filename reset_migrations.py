import os
import shutil

def oswalk():
  # Speed results:
  # os.path.join:                   1.6594289385000593, 1.6521514563999518
  # adding strings together:        1.65397772039978,   1.6509860470998319
  try:
    os.remove("db.sqlite3")
  except(FileNotFoundError):
    pass

  for dirpath, dirnames, filenames in os.walk("annotation_app/migrations"):
    for filename in filenames:
      if filename != '__init__.py':
        # os.remove(os.path.join(dirpath, filename))
        os.remove(dirpath + '/' + filename)

  os.system("python manage.py makemigrations")
  os.system("python manage.py migrate")

oswalk()

# def shrmtree(): # Speed results:  1.6614629764997517, 1.6542836995995458
#   try:
#     os.remove("db.sqlite3")
#   except(FileNotFoundError):
#     pass

#   try:
#     shutil.rmtree("annotation_app/migrations")
#   except(FileNotFoundError):
#     pass

#   os.mkdir("annotation_app/migrations")
#   with open("annotation_app/migrations/__init__.py", 'a') as f:
#     pass

#   os.system("python manage.py makemigrations")
#   os.system("python manage.py migrate")

# Speed test
# import timeit

# print(sum(timeit.repeat(shrmtree, repeat=10, number=1)) / 10.0)
# print(sum(timeit.repeat(oswalk, repeat=10, number=1)) / 10.0)
