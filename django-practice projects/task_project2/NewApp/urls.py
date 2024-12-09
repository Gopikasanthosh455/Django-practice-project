from django.urls import path
from NewApp import views


urlpatterns =[
    path('register/',views.Register,name="Register"),
    path('save_register/',views.Save_register,name="save_register"),
    path('display_reg/',views.display_reg,name="display_reg")
]