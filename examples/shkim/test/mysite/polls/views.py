from django.shortcuts import render
from polls.models import User

def index(request):
    return render(request, 'polls/index.html')
