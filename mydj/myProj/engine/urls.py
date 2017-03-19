from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^student/$',views.student),
    url(r'^account_log/$',views.acclog,name='account_log')
]