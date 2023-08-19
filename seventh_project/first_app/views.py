from django.shortcuts import render
from first_app.forms import StudentForm
from .models import Student,Teacher
# Create your views here.

def home(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form=StudentForm()
    return render(request,'home.html',{'form':form})

def showData(request):
    # student list for one teacher
    teacher=Teacher.objects.get(name='Rahim')
    students=teacher.student.all()
    for stud in students:
        print(stud.name)
    #teachers list for one student
    teacher=Student.objects.get(name='Adil')
    teachers=students.teacher.all()
    for tec in teachers:
        print(tec.name)
    return render(request,'show_data.html')