from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm

# Create your views here.

# Class based generic views

class TaskList(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class TaskDetail(DetailView):
        model = Task
        template_name = 'detail.html'
        context_object_name = 'task'

class TaskUpdate(UpdateView):
            model = Task
            template_name = 'edit.html'
            context_object_name = 'task'
            fields = ['name','priority','date']

            def get_success_url(self):
                return reverse_lazy('cbvdetail',kwargs={'pk':self.object})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Function based views

def home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        prio = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=prio,date=date)
        task.save()
    return render(request,'home.html',{'task':task1})
def delete(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'id':id})

def update(request,taskid):
    task = Task.objects.get(id=taskid)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})