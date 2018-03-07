# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SignupForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return HttpResponseRedirect("/confirm_your_email/")

    else:
        form=SignupForm()
    return render(request, "registration/sign_up.html", {'form': form})
