from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_gold', views.process_money),
    path('reset', views.reset)
]