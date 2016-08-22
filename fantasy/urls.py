from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.fantasy_index),
    url(r'^js_test', views.js_test),
]