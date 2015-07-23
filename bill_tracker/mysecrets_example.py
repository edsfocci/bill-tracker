# A good way to change your secrets is to do these in a temporary folder:
# django-admin.py startproject aaa && django-admin.py startproject bbb

# Then, find SECRET_KEY in the settings.py file, and replace the below secrets
# with new secrets. Delete the temporary folder afterwards.


# This is a required secret that Django uses to encrypt things
django_secret = '4nj@l_45tcv3i4-joo$x2bplk+a&&t3nb_5n2i6mc%orq8685t'

# This will serve as your psql user 'bill_tracker's password
psql_password = '(-^z2!4_8_ltz@@6*4ha3sk(69s5x!d@3wp4si(0zch_vku&je'
