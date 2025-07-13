from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def studentsView(request):
    students = {
        'id' : 1,
        'name' : 'kabir',
        'class' : "BSC"
    }
    
    return JsonResponse(students)