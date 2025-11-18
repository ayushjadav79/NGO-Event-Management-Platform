from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(
        next_page='/'
    ), name='admin_login'),

    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('ngo/', include('ngo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)