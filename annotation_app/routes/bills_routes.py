from django.conf.urls import url
from annotation_app.controllers import bills_controller
# Deprecated
from annotation_app import views


### Bills routes
# bills routes to controller actions below.
# bills handles the bill_list and adding bills

def bills(request):
  if request.method == 'GET':
    return views.bill_list(request)

  elif request.method == 'POST':
    return bills_controller.pull_bill(request)


### Bills URLs
urlpatterns = [

  url(r'^$', bills, name='bills'),
  url(r'^get-bill-info/$', bills_controller.get_bill_info,
    name='get_bill_info'),
  url(r'^get_bill_list/$', views.get_bill_list, name='get_bill_list'),
  # Deprecated
  url(r'^(?P<bill_id>\d+)/$', views.bill, name='bill'),

  # Deprecated
  url(r'^addbill/$', bills_controller.pull_bill, name='add_bill'),
]
