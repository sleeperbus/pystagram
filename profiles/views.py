# coding: utf-8
from __future__ import unicode_literals 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model 

# Create your views here.
def profile(request, username):
  User = get_user_model() 
  user = get_object_or_404(User, username=username)

  return render(request, 'profile.html', {'current_user': user,})


