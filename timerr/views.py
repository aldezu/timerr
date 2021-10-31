from django.shortcuts import render
from django import forms
from .models import Excersises
from .forms import AddForm
import itertools
# Create your views here.

def showForm(request):
    dat = Excersises.objects.all()
    return render(request, 'index.html', {'dat':dat})


def GoToTimer(request):
    #dat.reps = 11
    print(request.POST)
    if request.method == 'POST':
        form = request.POST.copy()
        del form['csrfmiddlewaretoken']
        form['tasksn'] = int(form['tasksn']) - 1 
        return render(request, 'timer.html', {'form':form})
    else:
        Form = AddForm()
        return render(request, 'index.html', {'Form':Form})

#def SelectTasks(request):
#    return render()