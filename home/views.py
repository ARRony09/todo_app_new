from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Createtodo,UserInformation
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
#from .models import 
# Create your views here.

def home(request):
    return render(request,"home/home.html")

def create(request):
    if request.method == "POST":
        title=request.POST['title']
        memo=request.POST['memo']
        #check_important=request.POST['check_important']
        try:
            check_important = request.POST['check_important']
        except MultiValueDictKeyError:
            check_important = False

        if check_important == 'on':
            check_important = True
        else:
            check_important = False
        create_new=Createtodo(title=title,memo=memo,important=check_important)
        create_new.save()
    return render(request,"home/create.html")

def current(request):
    alltodos=Createtodo.objects.filter(datecompleted__isnull=True)
    params = {'alltodos':alltodos}
    return render(request,"home/current.html",params)

def completed(request):
    completedtodos=Createtodo.objects.filter(datecompleted__isnull=False).order_by('-datecompleted')
    params={'completedtodos':completedtodos}
    return render(request,"home/completed.html",params)

def todo_details(request,pk):
    new_todo=Createtodo.objects.get(id=pk)
    params={'new_todo':new_todo}
    return render(request,"home/todo_details.html",params)

def delete(request,pk):
    todo=Createtodo.objects.filter(id=pk)
    todo.delete()
    return redirect('/current')

def completetodo(request,pk):
    todoview=get_object_or_404(Createtodo,id=pk)
    todoview.datecompleted=timezone.now()
    todoview.save()
    return redirect('current')

def handlelogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Login")
            return redirect('home')
        else:
            messages.error(request,"Invalid Email or password")
    return render(request,'home/login.html')

def handlesignup(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["pass1"]
        confirm_password=request.POST["pass2"]
        if len(username)<2:
            messages.warning(request,"Username should more than 1 latter")
            return render(request,'home/signup.html')
        if len(email)<8:
            messages.warning(request,"Email should more than 8 latter")
            return render(request,'home/signup.html')
        if password!=confirm_password:
            messages.warning(request,"Password didn't match. Try again")
            return render(request,'home/signup.html')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"Successfully account created")
    else:
        messages.warning(request,"Invalid")
    return render(request,'home/signup.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully logout")
    return redirect('home')

