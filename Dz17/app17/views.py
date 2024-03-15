from django.shortcuts import render, redirect
from app17.form import TaskCreateForm, Settings
from app17.models import *
from datetime import datetime

default_order = "title"
default_theme = 'black'


def not_view_func(type_of_action, title):
    action = Actions.objects.create(title=title, action=ActionType.objects.get(action_name=type_of_action), made_at=datetime.now())
    action.save()
    return 'pass'


def task_list_view(request):

    context = {'task_list': Task.objects.filter(status='in process').order_by(f'{default_order}')}
    return render(request, 'app17/tasklistview.html', context)


def task_detail_view(request, pk):
    context = {'task': Task.objects.get(pk=pk)}
    not_view_func('TaskDetail', Task.objects.get(pk=pk).title)
    return render(request, 'app17/taskdetailview.html', context)


def task_create_view(request):
    context = {}
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            not_view_func('TaskCreate', form.cleaned_data.get('title'))
            return redirect('task_list')
    form = TaskCreateForm()
    context['form'] = form
    return render(request, 'app17/taskcreateview.html', context)


def task_update_view(request, pk):
    context = {}
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, request.FILES, instance=Task.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            not_view_func('TaskUpdate', Task.objects.get(pk=pk).title)
            return redirect('task_list')
    form = TaskCreateForm(initial={
        'title':Task.objects.get(pk=pk).title,
        'description': Task.objects.get(pk=pk).description,
        'priority': Task.objects.get(pk=pk).priority,
        'deadline': Task.objects.get(pk=pk).deadline,
        'image': Task.objects.get(pk=pk).image,
    })
    context['form'] = form
    return render(request, 'app17/taskupdateview.html', context)


def task_delete_view(request, pk):
    task = Task.objects.get(pk=pk)
    not_view_func('TaskDelete', Task.objects.get(pk=pk).title)
    task.delete()
    return redirect('task_list')


def button_completed(request, pk):
    model = Task.objects.get(pk=pk)
    if model.status == 'in process':
        not_view_func('from_InProcess_to_Completed', Task.objects.get(pk=pk).title)
        model.status = 'completed'
        model.completed_at = datetime.now()
        model.save()
    else:
        not_view_func('from_Completed_to_InProcess', Task.objects.get(pk=pk).title)
        model.status = 'in process'
        model.completed_at = None
        model.save()

    print(Task.objects.get(pk=pk).status, Task.objects.get(pk=pk).completed_at)

    if model.status == 'in process':
        return redirect('task_history')

    else:
        return redirect('task_list')


def task_history_view(request):
    context = {
        'task_list': Task.objects.filter(status='completed')
    }
    return render(request, 'app17/taskhistoryview.html', context)


def action_history_view(request):
    context = {'action_list':Actions.objects.all()}
    return render(request, 'app17/actionhistoryview.html', context)


def settings(request):
    global default_order
    global default_theme
    context = {}
    if request.method == 'POST':
        form = Settings(request.POST)
        if form.is_valid():


            default_order = form.cleaned_data.get('order')
            default_theme = form.cleaned_data.get('theme')
            clear_task_history = form.cleaned_data.get('clear_task_history')
            clear_action_history = form.cleaned_data.get('clear_action_history')

            if clear_task_history:
                Task.objects.filter(status='completed').delete()
            if clear_action_history:
                actions = Actions.objects.all()
                actions.delete()
            return  redirect('task_list')
    context['form'] = Settings(initial={'order':default_order, 'theme':default_theme})

    return render(request, 'app17/settings.html', context)
