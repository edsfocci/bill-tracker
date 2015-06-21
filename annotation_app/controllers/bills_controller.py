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

def add_bill(request):
  if request.method == 'POST':
    form = BillForm(request.POST)

    if form.is_valid():
      data = form.cleaned_data
      bill_num = data["number"]
      bill = Bill.objects.filter(number=bill_num)
      # If you find bill in the database, it is the first element in QuerySet
      if bill:
          bill = bill[0]
      # If bill is not in the database, pull it from TLO website
      if not bill: #move this to bill_parse.py
        data = form.cleaned_data
        bill = Bill()
        bill.number = data['number']
        bill_import = Bill_Import()
        bill_import.set_bill_num(str(bill.number))
        bill_import.pull_billtext()
        bill_list = bill_import.billtext
        bill.text = Bill.serialize(bill_list)
        bill_import.pull_history()
        bill_import.set_data()
        bill.authors = Bill.serialize(bill_import.authors)
        bill.coauthors = Bill.serialize(bill_import.coauthors)
        bill.subjects = Bill.serialize(bill_import.subjects)
        bill.cosponsors = Bill.serialize(bill_import.cosponsors)
        bill.sponsors = Bill.serialize(bill_import.sponsors)
        bill.save()

        save_authors(bill, bill_import.authors)
        save_subjects(bill, bill_import.subjects)

def get_bill_list(request):
  #TODO optimize
  data = serializers.serialize("json", Bill.objects.all())
  #print(data)
  return HttpResponse(data)

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

def bill_list(request):
  return render(request, 'bill-list.html')