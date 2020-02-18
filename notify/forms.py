# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 17:00
# @Author  : MLee
# @File    : forms.py
from django.forms import ModelForm

from .models import SubscriberInfoModel


class SubscriberModelForm(ModelForm):
    class Meta:
        model = SubscriberInfoModel
        fields = ["email", ]
