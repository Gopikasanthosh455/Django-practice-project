from django.urls import path
from LumApp import views


urlpatterns=[
    path('AddStudent/',views.AddStudent,name="AddStudent"),
    path('Save_student/',views.Save_student,name="Save_student"),
    path('Display_Student/',views.Display_student,name="Display_Student"),
    path('Edit_student/<int:stud_id>/',views.edit_student,name="Edit_student"),
    path('update_student/,<int:stud_id>/',views.delete_student,name="delete_student"),
    path('Add_course/',views.Add_course,name="Add_course"),
    path('save_course/',views.save_course,name="save_course"),
    path('display_course/',views.display_course,name="display_course"),
    path('Edit_course/<int:course_id>/',views.Edit_course,name="Edit_course"),
    path('update_course/<int:course_id>/',views.update_course,name="update_course"),
    path('delete_course/<int:course_id>/',views.delete_course,name="delete_course")
]