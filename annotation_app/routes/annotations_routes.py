from django.conf.urls import url
from annotation_app.controllers import annotations_controller


### Annotations routes
# annotations and annotation routes to controller actions below.
# annotations handles the annotation_list and creating a new annotation
# annotation handles individual annotations that have an id (update and delete)

def annotations(request):
  if request.method == 'GET':
    return annotations_controller.list(request)

  elif request.method == 'POST':
    return annotations_controller.create_update(request)


def annotation(request, annotation_id):
  if request.method == 'PUT':
    return annotations_controller.create_update(request, annotation_id)

  elif request.method == 'DELETE':
    return annotations_controller.delete(annotation_id)

  # elif request.method == 'GET':
  #   try:
  #     annotation = Annotation.objects.get(id = annotation_id)
  #   except Annotation.DoesNotExist:
  #     raise Http404
  #   comment_list = annotation.comment_set.all()
  #   context = {'annotation': annotation, 'comment_list': comment_list}
  #   return render(request, 'annotation.html', context)


### Annotations URLs
urlpatterns = [

  url(r'^$', annotations, name='annotations'),
  url(r'^(?P<annotation_id>\d+)/$', annotation, name='annotation'),

  # Deprecated
  # url(r'^addannotation/$', views.add_annotation, name='add_annotation'),
]
