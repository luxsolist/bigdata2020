from django.urls import path
from . import views

urlpatterns = [
    path('tour/', views.tour_first, name='index'),
    path('search/', views.tour_search, name='search'),
    path('detail/',views.detail, name='detail'),
]
