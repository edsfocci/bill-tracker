import bs4
from django.core import serializers
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
import requests
from annotation_app.bill_parse import Bill_Import
from django.core import serializers
 #get_history,

from annotation_app.models import Bill, Senator, Subject
from annotation_app.forms import BillForm
import json