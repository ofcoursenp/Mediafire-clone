from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Upload

# Create your views here.

@login_required(login_url='login')
def index(req):
    if req.method == 'POST':
        file2 = req.FILES['file']
        document = Upload.objects.create(file=file2,user=req.user)
        document.save()
    return render(req,'index.html')

@login_required(login_url='login')
def files(req):
    items = Upload.objects.filter(user=req.user)
    send = {'upload':items}
    return render(req,'files.html',send)




def loginPage(req):
    if req.user.is_authenticated:
        return redirect('home')

    else:
        if req.method == "POST":
            username=req.POST.get('username')
            password=req.POST.get('password')

            user = authenticate(req,username=username,password=password)
            print(username)
            print(password)

            if user is not None:
                login(req,user)
                return redirect('home')
            else:
                messages.info(req,'Username or Password is incorecct')


    return render(req,'login.html')

def logoutUser(req):
    logout(req)
    return redirect('login')



def register(req):
    if req.user.is_authenticated:
        return redirect('home')
    
    else:
        form = CreateUserForm()
        if req.method == "POST":
            form = CreateUserForm(req.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(req,f'Account was created sucessfully for {user} ')
                return redirect('login')    
    content = {'form':form}
    return render(req,'register.html',content)

