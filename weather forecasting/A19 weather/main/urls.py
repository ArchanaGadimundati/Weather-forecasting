from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns=[
        path('wheather',views.index,name="wheather"),
        path('',views.Home,name="home")
]
