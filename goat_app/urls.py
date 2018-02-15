from django.conf.urls import url
from goat_app import views

# TEMPLATE TAGGING
app_name = 'goat_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/', views.ImageList.as_view(), name='gallery'),
    url(r'^surprise/', views.surprise_goat, name='surprise_goat'),
    url(r'^goat/(?P<pk>\d+)/', views.ImageDetail.as_view(), name='detail'),
    url(r'^about/', views.about, name='about'),
    url(r'^ajax/validate_email/$', views.validate_email, name='validate_email'),
]
