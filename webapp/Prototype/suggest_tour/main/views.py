from django.shortcuts import render
from .models import TOURLIST_USER
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def main(request):
  return render(request, 'main/login.html')

def signup(request):
  return render(request, 'main/signup.html')

def signup_chk(request):
  if request.method == 'POST':
    user_id = request.POST.get("user_id")
    user_pw = request.POST.get("user_pw")
    user_name = request.POST.get("user_name")
    gender = request.POST.get("gender")
    email = request.POST.get("email")
    address = request.POST.get("address")

    account = TOURLIST_USER(
      user_id = user_id,
      user_pw = user_pw,
      user_name = user_name,
      gender = gender,
      email = email,
      address = address,
    )
    account.save()
    messages.info(request, "Account Created Successfully")
    return JsonResponse({"success": "True"}, status = 200)

def login_chk(request):
  if request.method == "POST":
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    if TOURLIST_USER.objects.filter(user_id=user_id).exists():
      if user_pw == TOURLIST_USER.objects.get(user_id=user_id).user_pw :
        user_name = TOURLIST_USER.objects.get(user_id=user_id).user_name
        save_session(request, user_name)
        return JsonResponse({"success": "True"}, status = 200)
      else:
        return JsonResponse({"error": "Incorrect Password"}, status = 401)
    else:
      return JsonResponse({"error": "ID not found"}, status = 401)

def save_session(request, user_name):
  request.session['user_name'] = user_name

def chk_id(request):
  if request.method == "POST":
    user_id = request.POST.get("user_id")
    if TOURLIST_USER.objects.filter(user_id=user_id).exists():
      return JsonResponse({"success": "False"}, status = 200)
    else:
      return JsonResponse({"success": 'True'}, status = 200)
