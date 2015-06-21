

def author_list(request):
  return render(request, 'author-list.html')

def get_author_bills(request):
  author_id = request.GET.get("id")
  #TODO optimize
  data = Senator.objects.get(id=author_id).bills.all()
  print(data)
  data = serializers.serialize("json", data)
  print(data)
  return HttpResponse(data)

def get_author_list(request):
  #TODO optimize
  data = serializers.serialize("json", Senator.objects.all())
  print(data)
  return HttpResponse(data)
def author(request, author_id):
  try:
    author = Senator.objects.get(id = author_id)
  except Senator.DoesNotExist:
    raise Http404
  context = {'author': author}
  return render(request, 'author.html', context)

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