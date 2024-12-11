from django.urls import path
from projectapp import views

urlpatterns=[
    path('student/',views.student,name="student"),
    path('save_student/',views.save_student,name="save_student"),
    path('display_student/',views.display_student,name="display_student"),
    path('Edit_student/<int:Stud_id>/',views.Edit_student,name="Edit_student"),
    path('update_student/<int:stud_id>/',views.update_student,name="update_student"),
    path('delete_student/<int:stud_id>/',views.delete_student,name="delete_student")
]