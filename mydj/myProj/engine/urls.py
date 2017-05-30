from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^regist/$',views.regist,name='regist'),
	url(r'^welcome/$',views.welcome,name='welcome'),
	url(r'^user_password/$',views.user_password,name='user_password'),
	url(r'^information/$',views.information,name='information'),
	url(r'^course_list/$',views.course_list,name='course_list'),
	url(r'^t_index/$', views.my_course, name='my_course'),
	url(r'^test/$', views.test, name='test'),
    url(r'^upload/$',views.upload,name='upload'),
]