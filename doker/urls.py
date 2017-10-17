from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^doker$', views.doker_page, name='doker_page'),
]
