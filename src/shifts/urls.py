from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'(?P<pk>\d+)/$', views.shift_new, name='shift_new'),
    url(r'^(?P<pk>\d+)/detail/$', views.DetailView.as_view(), name='detail'),
    url(r'(?P<pk>\d+)/detail/new/$', views.run_new, name='run_new'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='group_new'),
]