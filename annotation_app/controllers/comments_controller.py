from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from annotation_app.models import Comment, Annotation
from annotation_app.forms import CommentAddForm, CommentEditForm

def add_comment(request):
  if request.method == 'GET':
    form = CommentAddForm(initial={'annotation': request.POST['add_for']})
    return render(request, 'commentform.html', {'form': form, 'method': 'add'})
  elif request.method == 'POST':
    form = CommentAddForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      comment = Comment()
      comment.annotation = Annotation.objects.get(id = data['annotation'])
      comment.text = data['text']
      comment.save()
      return HttpResponseRedirect('/comments/%d/' % comment.id)
  raise Http404

def comment(request, comment_id):
  try:
    comment = Comment.objects.get(id = comment_id)
  except Comment.DoesNotExist:
    raise Http404
  context = {'comment': comment}
  return render(request, 'comment.html', context)

def edit_comment(request, comment_id):
  try:
    comment = Comment.objects.get(id = comment_id)
  except Comment.DoesNotExist:
    raise Http404

  if request.method == 'POST':
    form = CommentEditForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      comment.text = data['text']
      comment.save()
      return HttpResponseRedirect('/comments/%d/' % comment.id)
  else:
    form = CommentEditForm(initial={'id': comment.id,
      'annotation': comment.annotation.id, 'text': comment.text})
  return render(request, 'commentform.html',
    {'form': form, 'method': 'edit', 'id': comment.id})