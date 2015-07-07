from django.conf.urls import url
# Deprecated
from annotation_app import views


### Authors URLs
urlpatterns = [

  url(r'^$', views.author_list, name='authors'),
  url(r'^get_author_list/$', views.get_author_list, name='get_author_list'),
  url(r'^get_author_bills/$', views.get_author_bills, name='get_author_bills'),
  url(r'^(?P<author_id>\d+)/$', views.author, name='author'),#model for this needs to be changed to inlude more than one bill.
]
