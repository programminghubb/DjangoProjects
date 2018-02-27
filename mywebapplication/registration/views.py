# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# Create your views here.


def sign_up(request):
    return render(request, 'registration/sign_up.html')
