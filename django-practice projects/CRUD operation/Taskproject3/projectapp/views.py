from django.shortcuts import render, redirect

from projectapp.models import studentDB


# Create your views here.
def student(request):
    return render(request,"student.html")
def save_student(request):
    if request.method=="POST":
        a=request.POST.get('Name')
        b=request.POST.get('Age')
        c=request.POST.get('Place')
        d=request.POST.get('Mobile')
        e=request.POST.get('Address')
        f=request.POST.get('Course')
        g=request.POST.get('Institute')
        h=request.POST.get('Duration')
        obj=studentDB(Name=a,Age=b,Place=c,Mobile_number=d,Address=e,Course=f,Institute=g,Course_duration=h)
        obj.save()
        return redirect(student)
def display_student(request):
    data=studentDB.objects.all()
    return render(request,"display_student.html",{"data":data})
def Edit_student(request,Stud_id):
    data=studentDB.objects.get(id=Stud_id)
    return render(request,"Edit_student.html",{"data":data})
def update_student(request,stud_id):
    if request.method=="POST":
        s_name=request.POST.get('Name')
        s_age=request.POST.get('Age')
        s_place=request.POST.get('Place')
        s_mobile=request.POST.get('Mobile')
        s_address=request.POST.get('Address')
        s_course=request.POST.get('Course')
        s_institute=request.POST.get('Institute')
        s_duration=request.POST.get('Duration')
        studentDB.objects.filter(id=stud_id).update(Name=s_name,Age=s_age,Place=s_place,Mobile_number=s_mobile,Address=s_address,Course=s_course,Institute=s_institute,Course_duration=s_duration)
        return redirect(display_student)
def delete_student(request,stud_id):
    s=studentDB.objects.filter(id=stud_id)
    s.delete()
    return redirect(display_student)