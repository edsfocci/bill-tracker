import bs4
from django.core import serializers
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
import requests
from annotation_app.bill_parse import Bill_Import
from django.core import serializers
 #get_history,

from django.http import Http404, HttpResponse
from annotation_app.models import Annotation, Bill
from annotation_app.forms import AnnotationAddForm, AnnotationEditForm
import re, json

from annotation_app.models import Bill, Senator, Subject
from annotation_app.forms import BillForm
import json

from annotation_app.controllers.save_bill_info import save_bill, save_authors, save_subjects

def pull_bill_text(request):
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
			if not bill:#is this supposed to be an elif?
				bill = save_bill(bill_num)
			if 'format' in request.POST:
				return HttpResponse(serializers.serialize(request.POST['format'],[bill]))
			else:
				return HttpResponseRedirect('/bills/%d/' % bill.id)
	else:
		form = BillForm()
		return render(request, 'addbill.html', {'form': form})