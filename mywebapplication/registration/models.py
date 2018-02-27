# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SignUp(models.Model):
    first_name = models.CharField(max_length=30, blank=False, help_text='Insert your First Name')
    last_name = models.CharField(max_length=30, blank=False, help_text='Insert your Last Name')
    email = models.EmailField(max_length=254, blank=False, help_text='Insert a valid email address.')
    password = models.CharField(max_length=24, blank=False, help_text='Insert new password')


