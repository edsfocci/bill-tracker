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