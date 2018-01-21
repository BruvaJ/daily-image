from django.conf.urls import url
from goat_app import views

# TEMPLATE TAGGING
app_name = 'goat_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^about/', views.about, name='about'),
]
