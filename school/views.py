from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    students_objects = Student.objects.all()
    template = 'school/students_list.html'
    # for student in students_objects:
    #     print(student.teacher)
    context = {'object_list': students_objects}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
