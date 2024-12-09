from django.shortcuts import render, redirect

from PracticeApp.models import stud_Db


# Create your views here.
def stud_reg(request):
    return render(request,"student_reg.html")
def save_stud(request):
    if request.method == "POST":
        a=request.POST.get('Name')
        b=request.POST.get('Class')
        c=request.POST.get('Department')
        d=request.POST.get('College')
        obj=stud_Db(Name=a,Class=b,Department=c,College=d)
        obj.save()
        return redirect(stud_reg)
def Display_stud(request):
    data=stud_Db.objects.all()
    return render(request,"Display_stud.html",{"data":data})