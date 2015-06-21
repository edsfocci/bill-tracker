from annotation_app.models import Bill, Senator, Subject
from annotation_app.forms import BillForm
from django.core import serializers
from annotation_app.bill_parse import Bill_Import_Call

def save_bill(number):
	bill = Bill()
	bill_import = Bill_Import_Call(number)
	bill_list = bill_import.billtext
	bill.text = Bill.serialize(bill_list)
	bill.authors = Bill.serialize(bill_import.authors)
	bill.coauthors = Bill.serialize(bill_import.coauthors)
	bill.subjects = Bill.serialize(bill_import.subjects)
	bill.cosponsors = Bill.serialize(bill_import.cosponsors)
	bill.sponsors = Bill.serialize(bill_import.sponsors)
	bill.save()
	save_authors(bill, bill_import.authors)
	save_subjects(bill, bill_import.subjects)
	return(bill)

def save_authors(bill, authors):
  #TODO fix duplicate authors
  for author in authors:
      senator = Senator.objects.filter(name=author)
      # If this senator is not in the db, add her/him
      if not senator:
        senator = Senator()
        senator.name = author
        senator.committee = "comittee" # TODO fix hardcode
        senator.is_chair = False # TODO fix hardcode
        senator.save()
        # Associate this senator with imported bill
        senator.bills.add(bill)
        senator.save()

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