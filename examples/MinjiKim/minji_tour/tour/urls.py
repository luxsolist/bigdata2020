from django.urls import path
from . import views

appname = 'tour'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/',views.detail, name='detail')
]
