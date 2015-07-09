from django.http import Http404, HttpResponse
from annotation_app.models import Annotation, Bill
from annotation_app.forms import AnnotationAddForm, AnnotationEditForm
import re, json


### Controller actions
# These handle all the actual processing of requests
# get_list: get annotation_list for particular bill
# create_update: create or update a new or existing annotation
# delete: divides an annotation's id by zero, ending it's existence, forever

def get_list(request):
  bill = Bill.objects.get(id = request.COOKIES['bill_id'])
  annotations = bill.annotation_set.all()
  annotation_list = []
  counter = 1

  for annotation in annotations:
    data = {}
    data['id'] = annotation.id
    data['user'] = annotation.user or 'demoUser'
    created = annotation.created
    data['data_creacio'] = unix_time(created) if created else counter
    counter += 1000
    data['text'] = annotation.text
    data['quote'] = annotation.quote
    data['ranges'] = [{
      'startOffset': annotation.ranges_start_offset,
      'endOffset': annotation.ranges_end_offset,
      'start': annotation.ranges_start,
      'end': annotation.ranges_end
    }]
    data['tags'] = json.loads(annotation.tags) if annotation.tags else []
    read_perm = annotation.permissions_read
    data['permissions'] = {
      'read': json.loads(read_perm) if read_perm else [data['user']],
      'update': [data['user']],
      'delete': [data['user']],
      'admin': [data['user']]
    }
    annotation_list.append(data)
  return HttpResponse(json.dumps(annotation_list))


def create_update(request, annotation_id=None):
  input_data = json.loads(request.body.decode("utf-8"))
  input_data['tags'] = json.dumps(input_data['tags'])
  input_data['ranges_start_offset'] = input_data['ranges'][0]['startOffset']
  input_data['ranges_end_offset'] = input_data['ranges'][0]['endOffset']
  input_data['ranges_start'] = input_data['ranges'][0]['start']
  input_data['ranges_end'] = input_data['ranges'][0]['end']
  input_data['permissions_read'] = json.dumps(input_data['permissions']['read'])

  form = AnnotationEditForm(input_data) if annotation_id else \
    AnnotationAddForm(input_data)

  if form.is_valid():
    data = form.cleaned_data

    annotation = Annotation.objects.get(id = annotation_id) if annotation_id \
      else Annotation()
    annotation.user = data['user']
    bill = Bill.objects.get(id = input_data['bill_id'])
    annotation.bill = bill
    annotation.text = data['text']
    annotation.quote = data['quote']
    annotation.ranges_start_offset = data['ranges_start_offset']
    annotation.ranges_end_offset = data['ranges_end_offset']
    annotation.ranges_start = data['ranges_start']
    annotation.ranges_end = data['ranges_end']
    annotation.tags = data['tags']
    annotation.permissions_read = data['permissions_read']
    annotation.save()

    return HttpResponse("{}") if annotation_id else \
      HttpResponse('{"id":'+ str(annotation.id) +'}')
  else:
    return HttpResponse(status=400)


def delete(annotation_id):
  try:
    annotation = Annotation.objects.get(id = annotation_id)
  except Annotation.DoesNotExist:
    raise Http404

  annotation.delete()
  return HttpResponse("{}")


### Helper functions

# Converts datetime to milliseconds since epoch
import datetime
def unix_time(dt):
  naive = dt.replace(tzinfo=None)
  epoch = datetime.datetime.utcfromtimestamp(0)
  delta = naive - epoch
  return int(delta.total_seconds() * 1000)


### Deprecated
# def add_annotation(request):
#   if request.method == 'POST':
#     if 'add_for' in request.POST:
#       form = AnnotationAddForm()
#       return render(request, 'addannotation.html',
#         {'form': form, 'bill_id': request.POST['add_for']})
#     else:
#       form = AnnotationAddForm(request.POST)
#       if form.is_valid():
#         data = form.cleaned_data
#         r = Annotation()
#         r.bill_id = Bill.objects.get(id = request.POST['bill_id'])
#         r.text = data['text']
#         r.save()
#         return HttpResponseRedirect('/annotations/%d/' % r.id)
#   raise Http404
