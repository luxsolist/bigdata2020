from django.shortcuts import render
from .models import Accounts
from django.http import JsonResponse
# Create your views here.

def main(request):
  return render(request, 'main/login.html')

def signup(request):
  return render(request, 'main/signup.html')

def signup_chk(request):
  if request.method == 'POST':
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    user_name = request.POST['user_name']
    gender = request.POST['gender']
    email = request.POST['email']
    address = request.POST['address']

    if Accounts.objects.filter(user_id = user_id).exists():
      return JsonResponse({"error": "User already exists"}, status = 401)
    else:
      account = Accounts(
        user_id = user_id,
        user_pw = user_pw,
        user_name = user_name,
        gender = gender,
        email = email,
        address = address,
      )
      account.save()

def login_chk(request):
  if request.method == "POST":
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    if Accounts.objects.filter(user_id=user_id).exists():
      if user_pw == Accounts.objects.get(user_id=user_id).user_pw :
        user_name = Accounts.objects.get(user_id=user_id).user_name
        save_session(request, user_name)
        return JsonResponse({"success": True}, status = 200)
      else:
        return JsonResponse({"error": "Incorrect Password"}, status = 401)
    else:
      return JsonResponse({"error": "ID not found"}, status = 401)

def save_session(request, user_name):
  request.session['user_name'] = user_name

def chk_id(request):
  if request.method == "POST":
    user_id = request.POST.get("user_id")
      if Accounts.objects.filter(user_id=user_id).exists():
        return JsonResponse({"success": "False"}, status = 200)
      else:
        return JsonResponse({"success": 'True'}, status = 200)
