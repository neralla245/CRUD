from django.shortcuts import render,redirect
from .models import students
# Create your views here.
def details(request):
    student=students.objects.all()
    return render(request,'table.html',{'student':student})
def insert(request):
    if request.method=='POST':
        name=request.POST['name']
        rollno=request.POST['rollno']
        college=request.POST['college']
        student=students(name=name,rollno=rollno,college=college)
        student.save()
        return redirect('/')
    return render(request,'insert.html')
def deleteview(request,id):
    student=students.objects.get(id=id)
    student.delete()
    return redirect('/')
def updateview(request,id):
    student=students.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        rollno = request.POST['rollno']
        college = request.POST['college']
        student.name=name
        student.rollno=rollno
        student.college=college
        student.save()
        return redirect('/')
    return render(request,'update.html',{'student':student})