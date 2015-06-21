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

def get_subject_bills(request):
  subject_id = request.GET.get("id")
  #TODO optimize
  data = Subject.objects.get(id=subject_id).bills.all()
  print(data)
  data = serializers.serialize("json", data)
  print(data)
  return HttpResponse(data)
def get_subject_list(request):
  #TODO optimize
  data = serializers.serialize("json", Subject.objects.all())
  print(data)
  return HttpResponse(data)
def subject(request, subject_id):
  try:
    subject = Subject.objects.get(id = subject_id)
  except Subject.DoesNotExist:
    raise Http404
  context = {'subject': subject}
  return render(request, 'subject.html', context)