from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.shift_list, name='shift_list'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^run/new/$', views.run_new, name='run_new'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='group_new'),
]