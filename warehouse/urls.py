from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^warehouse$', views.warehouse_page, name='warehouse_page'),
    url(r'^warehouse/warm$', views.warehouse_warm, name='warehouse_warm'),
    url(r'^warehouse/cold$', views.warehouse_cold, name='warehouse_cold'),
    url(r'^warehouse/manufacture$', views.warehouse_manufacture, name='warehouse_manufacture'),
    url(r'^warehouse/open$', views.warehouse_open, name='warehouse_open'),
]
