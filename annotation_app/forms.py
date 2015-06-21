from django import forms

class BillForm(forms.Form):
  number = forms.IntegerField(label='number')

class BillAddForm(forms.Form):
  text = forms.CharField(label='text')

class BillEditForm(BillAddForm):
  id = forms.IntegerField(label='id', widget=forms.HiddenInput)

class AnnotationAddForm(forms.Form):
  user = forms.CharField(label='user')
  bill = forms.IntegerField(label='bill', widget=forms.HiddenInput)
  text = forms.CharField(label='text')
  quote = forms.CharField(label='quote')

  ranges_start_offset = forms.IntegerField(label='ranges_start_offset')
  ranges_end_offset = forms.IntegerField(label='ranges_end_offset')

  tags = forms.CharField(label='tags')

  permissions_read = forms.CharField(label='permissions_read')

class AnnotationEditForm(AnnotationAddForm):
  id = forms.IntegerField(label='id', widget=forms.HiddenInput)

class CommentAddForm(forms.Form):
  annotation = forms.IntegerField(label='annotation', widget=forms.HiddenInput)
  text = forms.CharField(label='text')

class CommentEditForm(CommentAddForm):
  id = forms.IntegerField(label='id', widget=forms.HiddenInput)
