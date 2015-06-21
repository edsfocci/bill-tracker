import bs4
from django.core import serializers
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
import requests
from annotation_app.bill_parse import Bill_Import
from django.core import serializers
 #get_history,

from annotation_app.controllers.bills_controller import pull_bill_text
from annotation_app.models import Bill, Senator, Subject
from annotation_app.forms import BillForm
import json

# Deprecated
# def index(request):
#   return render(request, 'base.html')

def bill_list(request):
  return render(request, 'bill-list.html')

def subject_list(request):
  return render(request, 'subject-list.html')

def author_list(request):
  return render(request, 'author-list.html')

def add_bill(request):
  return pull_bill_text(request)


def save_subjects(bill, subjects):
  #TODO fix duplicate subjects
  for subject_name in subjects:
    subject = Subject.objects.filter(name=subject_name)
    # If this subject is not in the db, add her/him
    if not subject:
      subject = Subject()
      subject.name = subject_name
      subject.save()
      # Associate this subject with imported bill
      subject.bills.add(bill)
      subject.save()
#do we need get_bill_text?      
'''
def get_bill_text(number):

  if not number.isalnum():
    None
  # Queries only senate bills in legislative session 84R
  url = "http://www.capitol.state.tx.us/tlodocs/84R/billtext/html/SB000" + number + "I.htm"
  #this suffix changes depending on what stage the bill is at. we could give them an option

  res = requests.get(url)
  if not res.status_code == requests.codes.ok:
    return None

  html = bs4.BeautifulSoup(res.text)
  clean_text = html.get_text()
  # this is actually a list of sentences
  sentence_list = clean_text.split('.')
  span_text = ""
  span_id = 0

  for sentence in sentence_list:
    modified_sentence = sentence.replace('\n',"").replace('\t',"").replace('\xa0',"").replace('\r',"")
    span = '<span id=' + str(span_id) + '>' + modified_sentence + '</span>'
    span_text += span
    span_id += 1

  return span_text
'''

@ensure_csrf_cookie
def bill(request, bill_id):
  try:
    bill = Bill.objects.get(id = bill_id)
  except Bill.DoesNotExist:
    raise Http404
  # annotation_list = bill.annotation_set.all()
  bill.text = text_frontend(bill.text)
  authors = Bill.deserialize(bill.authors)
  subjects = Bill.deserialize(bill.subjects)
  context = {'bill': bill, 'authors': authors, 'subjects': subjects }#, 'annotation_list': annotation_list}
  return render(request, 'bill.html', context)

@ensure_csrf_cookie
def author(request, author_id):#model for this needs to be changed to inlude more than one bill.
  try:
    author = Senator.objects.get(id = author_id)
  except Senator.DoesNotExist:
    raise Http404
  context = {'author': author}
  return render(request, 'author.html', context)
#what is this cookie?
@ensure_csrf_cookie
#pipes a subject to the front end
def subject(request, subject_id):
  try:
    subject = Subject.objects.get(id = subject_id)
  except Subject.DoesNotExist:
    raise Http404
  context = {'subject': subject}
  return render(request, 'subject.html', context)
#pipes all bills to front end.
def get_bill_list(request):
  #TODO optimize
  data = serializers.serialize("json", Bill.objects.all())
  #print(data)
  return HttpResponse(data)
# pipes all subjects to front end.
def get_subject_list(request):
  #TODO optimize
  data = serializers.serialize("json", Subject.objects.all())
  print(data)
  return HttpResponse(data)
#pipes authors to front end
def get_author_list(request):
  #TODO optimize
  data = serializers.serialize("json", Senator.objects.all())
  print(data)
  return HttpResponse(data)
#pipes bills by author to the front end.
def get_author_bills(request):
  author_id = request.GET.get("id")
  #TODO optimize
  data = Senator.objects.get(id=author_id).bills.all()
  print(data)
  data = serializers.serialize("json", data)
  print(data)
  return HttpResponse(data)

#pipes subjects to the front end.
def get_subject_bills(request):
  subject_id = request.GET.get("id")
  #TODO optimize
  data = Subject.objects.get(id=subject_id).bills.all()
  print(data)
  data = serializers.serialize("json", data)
  print(data)
  return HttpResponse(data)


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
