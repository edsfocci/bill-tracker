from django import forms


class BillForm(forms.Form):
  number = forms.IntegerField()


class AnnotationAddForm(forms.Form):
  user = forms.CharField()
  bill_id = forms.IntegerField(widget=forms.HiddenInput)
  text = forms.CharField()
  quote = forms.CharField()

  ranges_start_offset = forms.IntegerField()
  ranges_end_offset = forms.IntegerField()
  ranges_start = forms.CharField(required=False)
  ranges_end = forms.CharField(required=False)

  tags = forms.CharField()

  permissions_read = forms.CharField()

class AnnotationEditForm(AnnotationAddForm):
  id = forms.IntegerField(widget=forms.HiddenInput)


class CommentAddForm(forms.Form):
  annotation_id = forms.IntegerField(widget=forms.HiddenInput)
  text = forms.CharField()

class CommentEditForm(CommentAddForm):
  id = forms.IntegerField(widget=forms.HiddenInput)
