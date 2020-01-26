from django.shortcuts import render,redirect

# Create your views here.



def home(request):
	if request.user.is_authenticated:
		return redirect('todo-home')
	context = {
		'home' : True
	}
	return render(request, 'main_home/main_home.html',context)


def about(request):
	if request.user.is_authenticated:
		return redirect('todo-home')
	context = {
		'about' : True
	}
	return render(request, 'main_home/main_about.html',context)