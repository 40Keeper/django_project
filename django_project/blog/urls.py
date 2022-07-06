from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^S', views.home, name = 'home'),
    # url(r'^$', views.runbutton),
    # url(r'^home', views.runbutton, name = 'script')
]
