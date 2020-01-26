from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.



def signup(request):
	if request.user.is_authenticated:
		return redirect('todo-home')
	context = {
		'signup' : True
	}
	if request.method == 'POST':
		if request.POST['pswd'] == request.POST['cpswd']:
			try:
				user = User.objects.get(username=request.POST['uname'])
				context.update({
					'error': 'Username taken, Try another !!!'
				})
				return render(request, 'accounts/signup_page.html', context)
			except User.DoesNotExist:
				try:
					user = User.objects.get(email=request.POST['email'])
					context.update({
						'error': 'Email taken, Try another !!!'
					})
					return render(request, 'accounts/signup_page.html', context)
				except User.DoesNotExist:
					fname = request.POST['fname']
					lname = request.POST['lname']
					uname = request.POST['uname']
					email = request.POST['email']
					pswd = request.POST['pswd']
					user = User.objects.create_user(username=uname,password=pswd,email=email,first_name=fname,last_name=lname)
					print("User created---",user)
					auth.login(request,user)
					return redirect('todo-home')

		else:
			context.update({
				'error' : 'Password Not Matching !!!'
			})
			return render(request, 'accounts/signup_page.html', context)
	else:
		return render(request, 'accounts/signup_page.html',context)




def login(request):
	if request.user.is_authenticated:
		return redirect('todo-home')
	context = {
		'login' : True
	}
	if request.method == 'POST':
		user_name = request.POST['userN']
		user_pass = request.POST['userP']
		user = auth.authenticate(username=user_name,password=user_pass)
		if user is not None:
			auth.login(request,user)
			return redirect('todo-home')
		else:
			context.update({
				'error' : 'Invalid Credentials, try again'
			})
			return render(request, 'accounts/login_page.html', context)
	else:
		return render(request, 'accounts/login_page.html',context)



def logout(request):
	auth.logout(request)
	return redirect('main-home')

