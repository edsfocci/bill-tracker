from annotation_app.models import Bill
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from annotation_app.forms import BillForm

from annotation_app.controllers.save_bill_info import save_bill

def pull_bill(request):
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