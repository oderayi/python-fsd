
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^create/$', views.create, name='create'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
]
