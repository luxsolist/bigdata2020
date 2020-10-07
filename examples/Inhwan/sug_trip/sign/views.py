from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms.models import model_to_dict
from .models import User
from django.contrib import messages
import json

def join(request):
    print('join')
    user_id = request.POST.get('join_id')
    user_pw = request.POST.get('join_pw')
    user_sex = request.POST.get('join_sex')
    user_age = request.POST.get('join_age')
    user_add = request.POST.get('join_add')
    user_email = request.POST.get('join_email')
    user_fav_spot1 = request.POST.get('join_spot1')
    user_fav_spot2 = request.POST.get('join_spot2')
    user_fav_spot3 = request.POST.get('join_spot3')

    return HttpResponseRedirect('/join/')