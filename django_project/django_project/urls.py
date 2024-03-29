"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from requests import request
from users import views as user_views
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = "register"),
    path('profile/', user_views.profile, name = "profile"),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = "logout"),
    path('', blog_views.home, name = "home"),
    path('home/', blog_views.home, name = "home"),
    path('runrobot/',blog_views.runbutton1, name="run_robot"),
    path('stoprobot/',blog_views.stopbutton1, name="stop_robot"),
    path('runconveyor/',blog_views.runbutton2, name="run_conveyor"),
    path('stopconveyor/',blog_views.stopbutton2, name="stop_conveyor"),
    path('countingRPM/',blog_views.runbutton3, name="script3")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

