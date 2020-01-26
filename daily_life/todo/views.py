from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.contrib import messages
# Create your views here.



@login_required(login_url='login-page')
def home(request):
	context = {
		'index' : True
	}
	return render(request,'todo/todo_home.html',context)


@login_required(login_url='login-page')
def view_list(request):
	user_todo_data = Todo.objects.filter(user=request.user).order_by('-added_date')
	context = {
		'view_list': True,
		'data' : user_todo_data
	}
	return render(request, 'todo/view_list.html', context)


@login_required(login_url='login-page')
def add_new(request):
	context = {
		'add_new': True,
	}
	if request.method == 'POST':
		user_text = request.POST['user_text']
		user = Todo(user=request.user,text=user_text)
		user.save()
		messages.success(request, 'Save successfully !!!')
		return redirect('todo-add')
	else:
		return render(request, 'todo/add_new.html', context)



@login_required(login_url='login-page')
def delete(request,id):
	user = Todo.objects.filter(user=request.user,id=id)
	if not user:
		messages.error(request, 'Not found')
		return redirect('todo-view')
	user.delete()
	messages.success(request,'Delete Successfully')
	return redirect('todo-view')





















