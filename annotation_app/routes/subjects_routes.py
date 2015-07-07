from django.conf.urls import url
# Deprecated
from annotation_app import views


### Subjects URLs
urlpatterns = [

  url(r'^$', views.subject_list, name='subjects'),
  url(r'^get_subject_list/$', views.get_subject_list, name='get_subject_list'),
  url(r'^get_subject_bills/$', views.get_subject_bills,
    name='get_subject_bills'),
  url(r'^(?P<subject_id>\d+)/$', views.subject, name='subject'),
]
