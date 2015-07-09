from annotation_app.models import Bill, Subject


def create(subject_name, bill_id):
  subject = Subject.objects.filter(name = subject_name)

  if subject:
    subject[0].bills.add(Bill.objects.get(id = bill_id))
    return subject[0]

  else:
    subject = Subject()
    subject.name = subject_name
    subject.save()

    subject.bills.add(Bill.objects.get(id = bill_id))
    subject.save()
    return subject
