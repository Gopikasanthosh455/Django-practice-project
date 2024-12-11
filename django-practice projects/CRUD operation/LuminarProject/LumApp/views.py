from django.shortcuts import render, redirect

from LumApp.models import StudentDb, CourseDB


# Create your views here.
def AddStudent(request):
    return render(request,"AddStudent.html")
def Save_student(request):
    if request.method=="POST":
        a=request.POST.get('Name')
        b=request.POST.get('Age')
        c=request.POST.get('Place')
        d=request.POST.get('Course')
        e=request.POST.get('Mobile')
        f=request.POST.get('Email')
        g=request.POST.get('Address')
        obj=StudentDb(Name=a,Age=b,Place=c,Course=d,Mobile_number=e,Email=f,Address=g)
        obj.save()
        return redirect(AddStudent)
def Display_student(request):
    data=StudentDb.objects.all()
    return render(request,"Display_Student.html",{"data":data})
def edit_student(request,stud_id):
    data=StudentDb.objects.get(id=stud_id)
    return render(request,"Edit_student.html",{"data":data})
def update_student(request,studid):
    if request.method=="POST":
        s_name=request.POST.get('Name')
        s_age=request.POST.get('Age')
        s_place=request.POST.get('Place')
        s_course=request.POST.get('Course')
        s_mobile=request.POST.get('Mobile')
        s_email=request.POST.get('Email')
        s_address=request.POST.get('Address')
        StudentDb.objects.filter(id=studid).update(Name=s_name,Age=s_age,Place=s_place,Course=s_course,Mobile_number=s_mobile,Email=s_email,Address=s_address)
        return redirect(Display_student)
def delete_student(request,stud_id):
    student=StudentDb.objects.filter(id=stud_id)
    student.delete()
    return redirect(Display_student)
def Add_course(request):
    return render(request,"Add_Course.html")
def save_course(request):
    if request.method=="POST":
        course_a=request.POST.get('Course_name')
        course_b=request.POST.get('Duration')
        course_c=request.POST.get('Fees')
        course_d=request.POST.get('Institute_name')
        course_e=request.POST.get('Description')
        obj=CourseDB(Course_name=course_a,Duration=course_b,Fees=course_c,Institute=course_d,Description=course_e)
        obj.save()
        return redirect(Add_course)
def display_course(request):
    data=CourseDB.objects.all()
    return render(request,"Display_course.html",{"data":data})
def Edit_course(request,course_id):
    data=CourseDB.objects.get(id=course_id)
    return render(request,"Edit_course.html",{"data":data})
def update_course(request,course_id):
    if request.method=="POST":
        Course_name=request.POST.get('Course_name')
        Course_Duration=request.POST.get('Duration')
        Course_Fees=request.POST.get('Fees')
        Course_Institute=request.POST.get('Institute')
        Course_Description=request.POST.get('Description')
        CourseDB.objects.filter(id=course_id).update(Course_name=Course_name,Duration=Course_Duration,Fees=Course_Fees,Institute=Course_Institute,Description=Course_Description)
        return redirect(display_course)
def delete_course(request,course_id):
    course=CourseDB.objects.filter(id=course_id)
    course.delete()
    return redirect(display_course)
