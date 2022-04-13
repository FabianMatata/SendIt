from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from register import views as v
from django.contrib.auth import views as auth_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),

    path('', include('home.urls')),
    path('register/', v.register,name='register'),
    path('profile/', v.profile,name='profile'),

    path('login', auth_v.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', auth_v.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)