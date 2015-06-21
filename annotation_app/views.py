import bs4
from django.core import serializers
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
import requests
from annotation_app.bill_parse import Bill_Import
from django.core import serializers
 #get_history,

from annotation_app.models import Bill, Senator, Subject
from annotation_app.forms import BillForm
import json

#import controllers/bill_controller.py
#import  controllers/bill_controller.py

# Deprecated
# def index(request):
#   return render(request, 'base.html')

---BILL----
def bill_list(request):
  #moved to controllers/bills_controller.py

def get_bill_list(request):#does do something other than 
#bill_list?
  #TODO optimize
  #moved to controllers/bills_controller.py

def add_bill(request):
  #moved to controllers/bill_controller.py

@ensure_csrf_cookie
def bill(request, bill_id):
#moved to controllers/bills_controller.py

---SENATOR---
def author_list(request):
  #moved to controllers/senators_controller.py
#pipes authors to front end
def get_author_list(request):
  #does this do something different?
  #TODO optimize
  #moved to controllers/senators_controller.py

def save_authors(bill, authors):
  #moved to controllers/senators_controller.py

@ensure_csrf_cookie
def author(request, author_id):
#moved to controllers/senators_controller.py

#pipes bills by author to the front end.
def get_author_bills(request):
  #moved to controllers/senators_controller.py


---SUBJECT---
def subject(request, subject_id):
 #moved to controllers/subjects_controller.py
def subject_list(request):
  #moved to controllers/subjects_controller.py

def save_subjects(bill, subjects):
  #moved to controllers/subjects_controller.py

# pipes all subjects to front end.
def get_subject_list(request):
  #TODO optimize
  #moved to controllers/subjects_controller.py
#pipes subjects to the front end.
def get_subject_bills(request):
#moved to controllers/subjects_controller.py





















import re

# For the love of Linus, don't touch this!!!
def text_frontend(text):
  output = json.loads(text)[-1]
  output = output.replace(r'\u00a0', '&nbsp;').replace(r'\n', '')\
    .replace(r'\"', '"')#.replace('</center>', '</div>')\
    #.replace('<center>', '<div style="text-align:center;">')

  # if re.search('</span>', output):
  #   output = output.replace('</span>', '.</span>').replace('\\',"")
  #   output = str(re.sub(r'\{.+\}\s*', '', output))
  #   return output
  # else:
  #   sentence_list = output.split('.')
  #   sentence_list.pop()
  #   span_text = ""
  #   span_id = 1

  #   for sentence in sentence_list:
  #     modified_sentence = sentence.replace('\n',"").replace('\t',"").replace('\xa0',"").replace('\r',"").replace('\\',"")
  #     span = '<span id="' + str(span_id) + '">' + modified_sentence + '.</span>'
  #     span_text += span
  #     span_id += 1

  #   return span_text
  return output
