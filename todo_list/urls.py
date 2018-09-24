from django.conf.urls import url
from todo_list.views import *
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'todo_list'


urlpatterns = [
    url(r'^$', index, name='index'),
	url(r'^task/$', TaskListView.as_view()),
	url(r'^todo/(?P<pk>[0-9]+)/$', TaskListDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)