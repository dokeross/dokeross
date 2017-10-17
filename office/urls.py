from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^office$', views.office_page, name='office_page'),
]
