from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.t_index,name='t_index'),
	url(r'^t_login/$', views.t_login, name='t_login'),
	url(r'^t_logout/$', views.t_logout, name='t_logout'),
]