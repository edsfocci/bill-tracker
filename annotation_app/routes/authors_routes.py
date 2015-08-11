from django.conf.urls import url
# Deprecated
from annotation_app import views_deprecated


### Authors URLs
urlpatterns = [

  url(r'^$', views_deprecated.author_list, name='authors'),
  url(r'^get_author_list/$', views_deprecated.get_author_list, name='get_author_list'),
  url(r'^get_author_bills/$', views_deprecated.get_author_bills, name='get_author_bills'),
  url(r'^(?P<author_id>\d+)/$', views_deprecated.author, name='author'),#model for this needs to be changed to inlude more than one bill.
]
