from django.urls import path
from . import views

#This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
#name='post_list'		is the name of the URL that will be used to identify the view, this can be the same as the name of the view but it can also be something completely different.
urlpatterns = [
	path('', views.post_list, name='post_list'),
]