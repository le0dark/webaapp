from django.conf.urls import url
from firstapp import views

urlpatterns=[
     url('',views.index,name='index'),
 ]