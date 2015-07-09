from annotation_app.models import Bill, Senator


def create(senator_name, bill_id):
  senator = Senator.objects.filter(name = senator_name)

  if senator:
    senator[0].bills.add(Bill.objects.get(id = bill_id))
    return senator[0]

  else:
    senator = Senator()
    senator.name = senator_name
    senator.save()

    senator.bills.add(Bill.objects.get(id = bill_id))
    senator.save()
    return senator
