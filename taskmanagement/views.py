from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .import forms,models
from django.contrib.auth.models import Group
from .models import Task
from django.contrib import messages

# Create your views here.

# def good(request):
#     return HttpResponse('good morning')

def home_view(request):
    return render(request,'home.html')

def login_view(request):
    return render(request,'login.html')

def signin_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydic={'userForm':userForm,'customerForm':customerForm}
    
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save(commit=False)
            user.set_password(user.password)
            user.save()
        
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group=Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'signin.html',context=mydic)


def desktop_view(request):
    tasks = models.Task.objects.all()
    return render(request,'task.html',{'tasks':tasks})

def addtask_view(request):
    if request.method=="POST":
        taskform=forms.TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()
            messages.success(request, "Task added successfully!")

            return redirect('/accounts/profile/')
    else:
        taskform=forms.TaskForm()
    return render(request, 'addtask.html', {'taskform': taskform})

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks})

def update_task_view(request,pk):
    task=models.Task.objects.get(id=pk)
    if request.method=='POST':
        tasksForm=forms.TaskForm(request.POST,instance=task)
        if tasksForm.is_valid():
            tasksForm.save()
            return redirect('/accounts/profile/')
    else:
            tasksForm=forms.TaskForm(instance=task)
    return render(request,'update.html',{'tasksForm':tasksForm})

def delete_task_view(request,pk):
    task=models.Task.objects.get(id=pk)
    task.delete()
    return redirect('/accounts/profile/')
