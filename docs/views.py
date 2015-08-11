import random
from django.conf import settings
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail

def home(request):
  copy_list = [
    'Understand and create dialog ' +
      'about the proposed laws you care about.',

    'Help the community understand the proposed ' +
      'laws you feel strongly about.',

    'Follow newly proposed Texas laws —' +
      'for your piece of mind.'
  ]

  return render(request, 'home.html', {'copy': random.choice(copy_list)})

def about_us(request):
  return render(request, 'about-us.html')

def contact_us(request):
  return render(request, 'contact-us.html')

def blog(request):
  return render(request, 'blog.html')

def bill_listing(request):
  return render(request, 'bill-listing.html')


from django.shortcuts import render
from django.http import HttpResponseRedirect

def sample_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            send_mail('Subject here', 'Here is the message.', 'deeptiboddapati@gmail.com',
              ['deeptiboddapati@gmail.com'], fail_silently=True)
            # redirect to a new URL:
            return render(request, 'contact-us.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'sample_contact.html', {'form': form})

class NameForm(forms.Form):
    first_name = forms.CharField(label= 'First Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    number = forms.IntegerField(label='number', min_value=999999999, max_value = 10000000000)
    comment = forms.CharField(label = "Comment", max_length = 100)
