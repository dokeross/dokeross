from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
]
