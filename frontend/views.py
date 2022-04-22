from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignupForm

# Create your views here.
def list(request):
    return render(request,'list.html')

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
			return redirect('index')
        
	else:
		form = SignupForm()
	
	context = {
		'form':form,
	}

	return render(request, 'signup.html', context)
