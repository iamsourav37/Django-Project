from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Diary

# Create your views here.


@login_required(login_url='login-page')
def diary_index(request):
    context ={
        'index' : True
    }
    return render(request,"mydiary/diary_home.html",context)

@login_required(login_url='login-page')
def view_all_content(request):

    data = Diary.objects.filter(user=request.user)
    context = {
        'view_list': True,
        'data':data,
    }
    return render(request, "mydiary/view_content.html", context)

@login_required(login_url='login-page')
def add_new_content(request):
    context = {
        'add_new': True
    }
    if request.method == 'POST':
        user_title = request.POST['title']
        user_content = request.POST['content']
        print(user_title,user_content)
        obj = Diary(user=request.user,title=user_title,content=user_content)
        obj.save()
        messages.success(request,'Saved Successfully')
        return redirect('diary-add')
    else:
        return render(request, "mydiary/add_new.html", context)


@login_required(login_url='login-page')
def delete_content(request,id):
    obj = Diary.objects.filter(user=request.user, id=id)
    if not obj:
        messages.error(request, 'Not found')
        return redirect('diary-view')
    obj.delete()
    messages.success(request, 'Delete Successfully')
    return redirect('diary-view')
