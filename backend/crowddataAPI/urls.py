from django.urls import path,include
from crowddataAPI.views import *
urlpatterns = [
    path('/',home),
    path('/add',add)
]

## localhost:port/addtwo/