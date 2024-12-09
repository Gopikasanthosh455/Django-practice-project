from django.urls import path
from PracticeApp import views

urlpatterns=[
    path('stud_reg/',views.stud_reg,name="stud_reg"),
    path('save_stud/',views.save_stud,name="save_stud"),
    path('Display_stud/',views.Display_stud,name="Display_stud")
]