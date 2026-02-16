from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import Taskform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# kew jodi akjon user hoi tahole shei user er task gulo dekhabe
@login_required
def task_list(request):
    status_filter=request.GET.get('status','all')
    catagory_filter=request.GET.get('category','all')
    tasks=Task.objects.filter(user=request.user)
    
    if status_filter != 'all':
        tasks=tasks.filter(is_completed=(status_filter=='completed'))
    if catagory_filter != 'all':
        tasks=tasks.filter(category=catagory_filter)


    completed_task=tasks.filter(is_completed=True)
    pending_task=tasks.filter(is_completed=False)


    
    return render(request,'task_list.html',{
        
       
        'completed_task':completed_task,
        'pending_task':pending_task,
        'status_filter':status_filter,
        'category_filter':catagory_filter

    })
# akjon user task create korbe r sei task tar user hobe shei user
@login_required
def task_create(request):
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('task_list')
    else:
        form=Taskform()
    return render(request,'task_form.html',{'form':form})

@login_required
def task_detail(request,task_id):
    task=get_object_or_404(Task,id=task_id,user=request.user)
    return render(request,'task_detail.html',{'task':task})

# akjon user task delete korbe r sei task tar user hobe shei user
@login_required
def task_delete(request,task_id):
    task=get_object_or_404(Task,id=task_id,user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def task_mark_complete(request,task_id):
    task=get_object_or_404(Task,id=task_id,user=request.user)
    task.is_completed=True
    task.save()
    return redirect('task_list')

# register ba sign up view
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('task_list')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})