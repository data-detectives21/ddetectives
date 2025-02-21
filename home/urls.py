from django.urls import re_path,include
#from django.conf.urls import url
from home.views import *
from car_dealer_portal import *
from customer_portal import *

urlpatterns = [
    re_path(r'^$',home_page),
]
