from multiprocessing import context
from django.shortcuts import render

from educations.models import Student

# Create your views here.
def list_students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'list_students.html', context)