from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_ngo, name='register_ngo'),
    path('list/', views.ngo_list, name='ngo_list'),
]