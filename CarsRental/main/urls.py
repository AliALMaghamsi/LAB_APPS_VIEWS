from django.urls import path
from . import views

app_name='main'

urlpatterns=[
    path("",views.home,name='home'),
    path("about/",views.about,name='about'),
    path("password/generate/",views.password_gen,name='password_gen'),

]