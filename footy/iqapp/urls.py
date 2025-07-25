from django.urls import path
from .views import *

urlpatterns = [
    path('',welcome , name='welcome'), # API - POSTMAN 
    path('index/', index, name='index'),
    path('begin/',begin,name='begin'),
    path('inter/',inter,name='inter'),

    path('pr/',pr,name='pr'),

]