from django.shortcuts import render,redirect
from .forms import ToDoForm
from .models import ToDoModel
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
# Create your views here.


def home(request):
    return render(request,'home.html')

def incomplete_tasks(request):
    tasks = ToDoModel.objects.all()
    print(tasks)
    return render(request,'incomplete.html',{'data':tasks})

def completed_tasks(request):
    tasks= ToDoModel.objects.filter(is_completed=True)
    return render(request,'complete.html',{'data':tasks})


def complete_task(request, id):
    tasks= ToDoModel.objects.get(pk=id)
    tasks.is_completed = True
    tasks.save()
    return redirect('completedpage')

def add_tasks(request):
    if(request.method=='POST'):
        tasks = ToDoForm(request.POST)
        if tasks.is_valid():
            tasks.save()
            return redirect('incompletepage')
    else:
        tasks=ToDoForm()
    return render(request,'add.html',{'form':tasks})

def edit_task(request,id):
    tasks =ToDoModel.objects.get(pk=id)
    if(request.method=='POST'):
       form=ToDoForm(request.POST,instance=tasks)
       if form.is_valid():
            form.save()
            return redirect('incompletepage')
    else:
        form=ToDoForm(instance=tasks)
    return render(request,'add.html',{'form':form,'task':tasks})

def delete_task(request,id):
    tasks=ToDoModel.objects.get(pk=id).delete()
    return redirect('incompletepage')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('homepage')
    
