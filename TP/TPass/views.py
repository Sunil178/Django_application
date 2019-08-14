from django.shortcuts import render, redirect
from .models import Students
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
	all_records = Students.objects.all()
	return render(request, 'index.html', {'records': all_records})

def add(request):
	return render(request, 'add.html')

def addStudent(request):
	std = Students()
	std.enrollment = request.POST["enrollment"]
	std.name = request.POST["name"]
	std.save()
	return redirect('/')

# @csrf_protect
@csrf_exempt
def destroy(request, id):
	row = Students.objects.get(id=id)
	row.delete()
	return JsonResponse({'id': id})
# 
def editForm(request, id):
	row = Students.objects.get(id=id)
	return render(request, 'edit.html', {'row':row})

def edit(request, id):
	row = Students.objects.get(id=id)
	row.enrollment = request.POST["enrollment"]
	row.name = request.POST["name"]
	row.save()
	return redirect('/')