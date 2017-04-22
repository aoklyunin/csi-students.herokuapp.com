# -*- coding: utf-8 -*-
import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from sworks.forms import LoginForm, AttemptForm, AddTaskForm, AddAttemptForm, MarkForm, FloatForm
from .models import Student, Task, AttemptComment, Mark


# добавление задания
def addTask(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddTaskForm(request.POST)
            if form.is_valid():
                task_name = form.cleaned_data['task_name']
                pub_date = form.cleaned_data['pub_date']

                t = Task.objects.create(task_name=task_name,
                                        pub_date=pub_date,
                                        )
                t.save()
                messages.success(request, "Задание добавлено")

        data = {
            'task_name': '',
            'pub_date': datetime.date.today(),
            'ins_form': LoginForm()
        }

        return render(request, "sworks/addTask.html", {
            "task_form": AddTaskForm(initial=data),
            "login_form": LoginForm(),
            "user": request.user
        })
    else:
        return HttpResponseRedirect('/')


# организация обработки внешнего post-запроса
# для этого сделан декоратор @csrf_exempt
@csrf_exempt
def getTasks(request):
    if request.method == "POST":
        if request.POST["begin_date"] or request.POST["end_date"]:
            pickup_records = []
            for task in Task.objects.all():
                record = {"pub_date": task.pub_date,
                          "task_name": task.task_name}
                pickup_records.append(record)
            return JsonResponse({'tasks': pickup_records}, safe=False)
        return JsonResponse({'error': 'нет параметров дат'}, safe=False)
    return JsonResponse({'error': 'не тот запрос'}, safe=False)


# личный кабинет
def personal(request):
    # по пользователю получаем имя
    student = Student.objects.get(user=request.user)
    # список попыток, созданных текущем пользователем
    mark_list = Mark.objects.filter(student=student).order_by('task')
    sum = 0
    for mark in mark_list:
        sum += mark.m_value

    return render(request, "sworks/personal.html", {
        'login_form': LoginForm(),
        'mark_list': mark_list,
        'sum': sum,
    })


# классы ссылки
class hrefClass():
    def __init__(self, href, text):
        self.href = href
        self.text = text


# просмотр попытки по id
def mark_detail(request, mark_id):
    # ищем попытку с заданным id
    mark = Mark.objects.get(id=mark_id)
    # если пользователь хочет добавить комментарий
    if request.method == "POST":
        form = AttemptForm(request.POST)
        if form.is_valid():
            # текст комментария
            text = form.cleaned_data['text']
            # студент, написавший комментарий
            student = Student.objects.get(user=request.user)
            # создаём комментарий
            comment_object = AttemptComment.objects.create(isReaded=False, text=text, author=student)
            # сохраняем комментарий
            comment_object.save()
            mark.comment.add(comment_object)
    form = AttemptForm()
    return render(request, "sworks/mark_detail.html", {
        "mark": mark,
        "text_form": form,
        "login_form": LoginForm(),
        "user": request.user,
    })


def mark_needCheck(request, mark_id):
    # ищем попытку с заданным id
    mark = Mark.objects.get(id=mark_id)
    # студент, написавший комментарий
    student = Student.objects.get(user=request.user)
    if (mark.student == student) and ((mark.state == 0) or (mark.state == 1)):
        mark.state = 4
        mark.save()
    return HttpResponseRedirect('/personal/')


def mark_list(request):
    if request.user.is_staff:
        mark_list = Mark.objects.order_by('-add_date').filter(state=4)
        template = 'sworks/markList.html'
        context = {
            "mark_list": mark_list,
        }
        return render(request, template, context)
    else:
        return HttpResponseRedirect('/')


def mark(request, state_val, mark_id):
    print(state_val)
    if request.user.is_staff:
        print("staff")
        # ищем попытку с заданным id
        mark = Mark.objects.get(id=mark_id)
        if state_val == "1" or state_val == "2":
            mark.state = state_val
            mark.save()
            return HttpResponseRedirect('/mark/list/')
        if state_val == "3":
            print(request.POST)
            if request.method == "POST":
                form = FloatForm(request.POST)
                print(form)
                if form.is_valid():
                    # текст комментария
                    val = form.cleaned_data['val']
                    print(val)
                    mark.m_value = val
                    mark.state = state_val
                    mark.save()
            return HttpResponseRedirect('/mark/list_accepted/')

    return HttpResponseRedirect('/')


def mark_list_accepted(request):
    if request.user.is_staff:
        mark_list = Mark.objects.order_by('-add_date').filter(state=2)
        template = 'sworks/markAcceptedList.html'
        context = {
            "mark_list": mark_list,
            'form': FloatForm(initial = {'val':'0.0'}),
        }
        return render(request, template, context)
    else:
        return HttpResponseRedirect('/')


def mark_list_marked(request):
    if request.user.is_staff:
        mark_list = Mark.objects.order_by('student').filter(state=3)
        template = 'sworks/markMarkedList.html'
        context = {
            "mark_list": mark_list,
        }
        return render(request, template, context)
    else:
        return HttpResponseRedirect('/')