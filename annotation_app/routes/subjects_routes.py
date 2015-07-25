from django.conf.urls import url
# Deprecated
from annotation_app import views_deprecated


### Subjects URLs
urlpatterns = [

  url(r'^$', views_deprecated.subject_list, name='subjects'),
  url(r'^get_subject_list/$', views_deprecated.get_subject_list, name='get_subject_list'),
  url(r'^get_subject_bills/$', views_deprecated.get_subject_bills,
    name='get_subject_bills'),
  url(r'^(?P<subject_id>\d+)/$', views_deprecated.subject, name='subject'),
]
