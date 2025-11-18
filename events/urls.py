from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_event, name='add_event'),
    path('admin-list/', views.event_list_admin, name='event_list_admin'),
    path('', views.public_event_list, name='public_event_list'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,
        next_page='/'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='public_event_list'), name='logout'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/edit/', views.edit_event, name='edit_event'),
    path('event/<int:pk>/delete/', views.delete_event, name='delete_event'),
]