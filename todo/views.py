from django.shortcuts import render, HttpResponseRedirect
from .form import TodoRegistrations
from .models import FirstTodo


# Create your views here.

# add data and show
def addshow(request):
    if request.method == "POST":
        fm = TodoRegistrations(request.POST)
        if fm.is_valid():
            tl = fm.cleaned_data['title']
            dsc = fm.cleaned_data['description']
            st = fm.cleaned_data['status']
            dl = fm.cleaned_data['deadline']
            reg = FirstTodo(title=tl, status=st, deadline=dl,
                            description=dsc)
            reg.save()
            fm = TodoRegistrations()

    else:
        fm = TodoRegistrations()
    tudo = FirstTodo.objects.all()
    return render(request, 'todo/add_show.html', {'form': fm, 'tudo': tudo})

# delete data


def delete_data(request, id):
    if request.method == 'POST':
        pi = FirstTodo.objects.get(pk=id)

        pi.delete()
        return HttpResponseRedirect('/')


# update data
def update_data(request, id):
    if request.method == 'POST':
        pi = FirstTodo.objects.get(pk=id)
        fm = TodoRegistrations(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = FirstTodo.objects.get(pk=id)
        fm = TodoRegistrations(instance=pi)
    return render(request, 'todo/update.html', {'form': fm})
