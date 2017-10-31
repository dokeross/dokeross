from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^contacts$', views.contacts_page, name='contacts_page'),
]
