from django.shortcuts import render
import random

def home(request):
  copy_list = [
    'Understand, help others understand, and create ' +
      'dialog about the proposed laws you care about.',

    'Help the community understand the proposed ' +
      'laws you feel strongly for, or against.',

    'Know about the laws being proposed in your Texas ' +
      'State Legislature, for your piece of mind.'
  ]

  return render(request, 'home.html', {'copy': random.choice(copy_list)})
