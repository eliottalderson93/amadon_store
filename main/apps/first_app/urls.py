from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate$', views.generate),
    url(r'^result$', views.result),
    url(r'^create$', views.generate),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^delete$', views.destroy),
    # This line has changed! Notice that urlpatterns is a list, the comma is in
]   # anticipation of all the routes that will be coming soon
