from django.shortcuts import render
import random

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
