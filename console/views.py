#encoding: utf-8

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def sigin(request):
	# No need to login
	if(request.user.is_authenticated()):
		render(request, 'console.html')
	
	if(request.method == 'GET'):		
		return render(request, 'login.html')
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			return redirect('index')
		else:
			# invalid login			
			return render(request, 'login.html', {'error': 'Invalid username or password'})

def sigout(request):
    logout(request)
    return redirect('login')

def index(request):
    if(request.user.is_authenticated()):
        return render(request, 'console.html')
    else:
        return redirect('login')


        

