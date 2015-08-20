from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from annotation_app.models import Bill, Senator, Subject


def bill_list(request):
  return render(request, 'bill-list.html')

def subject_list(request):
  return render(request, 'subject-list.html')

def author_list(request):
  return render(request, 'author-list.html')


# Deprecated
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
  return render(request, 'bill_future.html', context)

@ensure_csrf_cookie
def author(request, author_id):
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
  data = serializers.serialize("json", Bill.objects.all())
  return HttpResponse(data)
# pipes all subjects to front end.
def get_subject_list(request):
  data = serializers.serialize("json", Subject.objects.all())
  return HttpResponse(data)
#pipes authors to front end
def get_author_list(request):
  data = serializers.serialize("json", Senator.objects.all())
  return HttpResponse(data)
#pipes bills by author to the front end.
def get_author_bills(request):
  author_id = request.GET.get("id")
  author_data = Senator.objects.get(id=author_id).bills.all()
  data = serializers.serialize("json", author_data)
  return HttpResponse(data)

#pipes subjects to the front end.
def get_subject_bills(request):
  subject_id = request.GET.get("id")
  subject_data = Subject.objects.get(id=subject_id).bills.all()
  data = serializers.serialize("json", subject_data)
  return HttpResponse(data)
