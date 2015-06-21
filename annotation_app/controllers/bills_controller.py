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

      if 'format' in request.POST:
        return HttpResponse(serializers.serialize(request.POST['format'],
          [bill]))
      else:
        return HttpResponseRedirect('/bills/%d/' % bill.id)
  else:
    form = BillForm()
  return render(request, 'addbill.html', {'form': form})

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
