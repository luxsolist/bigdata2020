from django.urls import path
from . import views

urlpatterns = [
    path('tour/', views.index, name='index'),
    path('detail/',views.detail, name='detail'),
    path('test/', views.test, name='test'),
]
