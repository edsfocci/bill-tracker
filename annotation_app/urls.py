"""bill_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
  https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
  1. Add an import:  from my_app import views
  2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
  1. Add an import:  from other_app.views import Home
  2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
  1. Add an import:  from blog import urls as blog_urls
  2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from annotation_app.controllers import comments_controller, clients_controller
# Deprecated
from annotation_app import views

urlpatterns = [
  # Comments routes
  url(r'^addcomment/$', comments_controller.add_comment, name='add_comment'),
  url(r'^comments/(?P<comment_id>\d+)/$', comments_controller.comment,
    name='comment'),
  url(r'^comments/(?P<comment_id>\d+)/edit/$', comments_controller.edit_comment,
    name='edit_comment'),

  # Frontend examples routes
  url(r'^example-client/$', clients_controller.example_client,
    name='example_client'),
  url(r'^megalith/$', clients_controller.megalith, name='megalith'),
]
