from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from annotation_app.models import Bill
from annotation_app.forms import BillForm
from annotation_app.helpers.bill_scrapers import scrape_bill_text,\
	scrape_bill_history
import json

# Deprecated
from annotation_app.controllers.save_bill_info_deprecated import save_bill


# Deprecated
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
				bill = save_bill(bill_num, data['chamber_origin'], data['session'])

			if 'format' in request.POST:
				return HttpResponse(serializers.serialize(request.POST['format'],
					[bill]))
			else:
				return HttpResponseRedirect('/bills/%d/' % bill.id)

	return HttpResponseRedirect('/')


@ensure_csrf_cookie
def get_one(request, bill_slug):
  chamber_origin = bill_slug[0].upper()
  number = bill_slug[2:]

  try:
    bill = Bill.objects.filter(chamber_origin = chamber_origin,
      number = number)[0]
  except Bill.DoesNotExist:
    raise Http404
  # annotation_list = bill.annotation_set.all()

  context = {'bill': bill}#, 'annotation_list': annotation_list}
  response = render(request, 'bill.html', context)
  response.set_cookie('bill_id', bill.id)
  return response


# Cater to deprecated route
def redirect_get_one(request, bill_id):
  bill = Bill.objects.get(id = bill_id)

  return HttpResponseRedirect('/bills/%sB%d/' % (bill.chamber_origin,
    bill.number))


def create(request):
  form = BillForm(request.POST)

  if form.is_valid():
    data = form.cleaned_data
    bill = Bill.objects.filter(chamber_origin = data['chamber_origin'],
      number = data['number'])

    # If you find bill in the database, it is the first element in QuerySet
    if bill:
      bill = bill[0]
    # If bill is not in the database, pull it from TLO website
    else:
      bill_text = scrape_bill_text(data)
      if bill_text == None:
        return HttpResponseRedirect('/')

      bill = Bill()
      bill.session = data['session']
      bill.chamber_origin = data['chamber_origin']
      bill.number = data['number']
      bill.text = bill_text

      from annotation_app.helpers.htmllogic import htmltext
      bill.text = htmltext(bill.text)
      bill.save()

    if 'format' in request.POST:
      return HttpResponse(serializers.serialize(request.POST['format'],
        [bill]))
    else:
      return HttpResponseRedirect('/bills/%sB%d/' % (bill.chamber_origin,
        bill.number))

  else:
    return HttpResponseRedirect('/')


def get_bill_info(request):
  if request.method == 'POST':
    from annotation_app.controllers import senators_controller,\
      subjects_controller

    bill = Bill.objects.get(id = request.POST['bill_id'])

    if len(bill.senator_set.all()) == 0 and len(bill.subject_set.all()) == 0:
      bill_data = {}
      bill_data['session'] = bill.session
      bill_data['chamber_origin'] = bill.chamber_origin
      bill_data['number'] = bill.number

      tmi_data = scrape_bill_history(bill_data)

      authors = tmi_data['authors'].split(' | ')
      # Deprecated
      bill.authors = json.dumps(authors)

      subjects = tmi_data['subjects']['subject']
      if type(subjects) != type([]):
        subjects = [subjects]
      # Deprecated
      bill.subjects = json.dumps(subjects)

      bill.save()

      for author in authors:
        senators_controller.create(author, bill.id)

      for subject in subjects:
        subjects_controller.create(subject, bill.id)

    elif len(bill.subject_set.all()) == 0:
      bill_data = {}
      bill_data['session'] = bill.session
      bill_data['chamber_origin'] = bill.chamber_origin
      bill_data['number'] = bill.number

      tmi_data = scrape_bill_history(bill_data)

      subjects = tmi_data['subjects']['subject']
      if type(subjects) != type([]):
        subjects = [subjects]
      # Deprecated
      bill.subjects = json.dumps(subjects)

      bill.save()

      for subject in subjects:
        subjects_controller.create(subject, bill.id)

    authors = bill.senator_set.all()
    authors = list(map(lambda author: author.name, authors))

    subjects = bill.subject_set.all()
    if len(subjects[0].name) == 1:
      for subject in subjects:
        bills = subject.bills.all()

        for bill in bills:
          bill.subject_set.remove(subject)

        subject.delete()

      return get_bill_info(request)

    subjects = list(map(lambda subject: subject.name, subjects))

    data = {}
    data['authors'] = authors
    data['subjects'] = subjects

    return HttpResponse(json.dumps(data))
  else:
    return HttpResponse("{}")
