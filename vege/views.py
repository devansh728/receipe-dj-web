from django.shortcuts import render,redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def receipes(request):
    print(request.user.is_authenticated)
    if request.method == "POST":
        data=request.POST   #it is for rendering data from fontend to backend
        receipe_image = request.FILES.get('receipe_image')
        receipe_desc = data.get('receipe_desc')
        receipe_name = data.get('receipe_name')
        #register this to admin in admin.py
        Receipe.objects.create(
            receipe_name= receipe_name,
            receipe_desc= receipe_desc,
            receipe_image= receipe_image
        )
        return redirect('/receipe/')
    
    queryset=Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipe': queryset}

    return render(request,'recipe.html',context)

def delete_receipe(request,id):
    receipe = Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('/receipe/')

def update_receipe(request,id):
    updated_receipe = Receipe.objects.get(id=id)
    if request.method =='POST':
        data = request.POST
        receipe_desc = data.get('receipe_desc')
        receipe_name = data.get('receipe_name')
        receipe_image = request.FILES.get('receipe_image')

        updated_receipe.receipe_name= receipe_name
        updated_receipe.receipe_desc= receipe_desc

        if receipe_image:
            updated_receipe.receipe_image = receipe_image

        updated_receipe.save()
        return redirect('/receipe/')
    context = {'receipe': updated_receipe}

    return render(request,'update_receipe.html',context)

def login_user(request):
    
    if request.method=='POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Username doesnt exist')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user) #for session
            return redirect('/receipe/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login/')
    return render(request,'login.html')   

def register_user(request):
    if request.method == "POST":
        data=request.POST   #it is for rendering data from fontend to backend

        firstname=data.get('firstname')
        lastname=data.get('lastname')
        username = data.get('username')
        password = data.get('password')
        
        userr = User.objects.filter(username=username)
        if userr.exists():
            messages.info(request,'Username Already exist')
            return redirect('/register/')
        #register this to admin in admin.py
        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account has been created succesfully')
        return redirect('/login/')
        
    return render(request,'register.html')