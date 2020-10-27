from django.urls import path
from . import views

urlpatterns = [
    path('tour/', views.index, name='index'),
    path('detail/',views.detail, name='detail'),
    path('test/', views.test, name='test'),
    path('get_latlng/',views.get_latlng, name='get_latlng')
]
