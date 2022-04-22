from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
from .serializers import TaskSerializer
from .models import Task
from App import serializers
from django.contrib.auth.models import User
from .forms import SignupForm


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'list':'/task-list',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',    
    }
    return Response(api_urls)
@api_view(['GET'])
def taskList(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(tasks,many=False)
    return Response(serializer.data)
    
    
@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    
    
    
    return Response('Item successfully deleted!')


def login(request):
  return render(request, 'login.html')

def Signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
            
        
            
   
            
			User.objects.create_user(username=username, email=email, password=password)
			return redirect('list')
        
	else:
		form = SignupForm()
	
	context = {
		'form':form,
	}

	return render(request, 'signup.html', context)
