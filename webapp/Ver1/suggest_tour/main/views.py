from django.shortcuts import render
from .models import TourlistUser
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
    gps_x = request.POST.get("mapx")
    gps_y = request.POST.get("mapy")

    account = TourlistUser(
      user_id = user_id,
      user_pw = user_pw,
      user_name = user_name,
      gender = gender,
      email = email,
      address = address,
      gps_x= gps_x,
      gps_y= gps_y,

    )
    account.save()
    messages.info(request, "Account Created Successfully")
    return JsonResponse({"success": "True"}, status = 200)

def login_chk(request):
  if request.method == "POST":
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    if TourlistUser.objects.filter(user_id=user_id).exists():
      if user_pw == TourlistUser.objects.get(user_id=user_id).user_pw :
        user_name = TourlistUser.objects.get(user_id=user_id).user_name
        gps_x = TourlistUser.objects.get(user_id=user_id).gps_x
        gps_y = TourlistUser.objects.get(user_id=user_id).gps_y
        save_session(request, user_name, gps_x, gps_y)
        return JsonResponse({"success": "True"}, status = 200)
      else:
        return JsonResponse({"success": "Incorrect Password"}, status = 200)
    else:
      return JsonResponse({"success": "ID not found"}, status = 200)

def save_session(request, user_name, gps_x, gps_y):
  request.session['user_name'] = user_name
  request.session['gps_x'] = gps_x
  request.session['gps_y'] = gps_y

def chk_id(request):
  if request.method == "POST":
    user_id = request.POST.get("user_id")
    if TourlistUser.objects.filter(user_id=user_id).exists():
      return JsonResponse({"success": "False"}, status = 200)
    else:
      return JsonResponse({"success": 'True'}, status = 200)
