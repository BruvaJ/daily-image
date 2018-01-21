from django.conf.urls import url
from goat_app import views

urlpatterns = [
    url(r'^$', views.index, name='home')
]
