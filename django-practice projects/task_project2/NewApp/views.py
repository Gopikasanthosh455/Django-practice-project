from django.shortcuts import render, redirect

from NewApp.models import RegisterDb


# Create your views here.
def Register(request):
    return render(request,"Register.html")
def Save_register(request):
    if request.method=="POST":
        a=request.POST.get('Name')
        b=request.POST.get('Age')
        c=request.POST.get('Place')
        d=request.POST.get('course')
        e=request.POST.get('Address')
        f=request.POST.get('email')
        g=request.POST.get('username')
        h=request.POST.get('password')
        i=request.POST.get('Mobile')
        obj=RegisterDb(Name=a,age=b,Place=c,Course=d,Address=e,Email=f,Username=g,Password=h,Mobile=i)
        obj.save()
        return redirect(Register)
def display_reg(request):
    data=RegisterDb.objects.all()
    return render(request,"Display_register.html",{'data':data})