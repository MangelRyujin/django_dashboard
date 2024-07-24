from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
# from apps.accounts.models import Profile
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm

from apps.accounts.models import User

# Dashboard view (index)
@login_required(login_url='/login/')
def dashboard_view(request):
    history = User.history.all()[:10]
    return render(request,'index.html',{"history":history})


# Log in view
def login_view(request):
    next_url = request.GET.get('next', '')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url =  request.POST.get('next_url','')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponse()
            response["HX-Redirect"]= next_url if next_url else '/'
            return response
        else:
            return HttpResponse(f"""
                                 <div class="alert alert-dismissible alert-danger d-flex align-items-center mb-0 mt-4 px-2 fade show" role="alert">
                      
                        <div class="small px-1 me-2 text-danger-emphasis">
                          Username or password incorrect
                        </div>
                        <span type="button" class="btn-close px-2" data-bs-dismiss="alert" aria-label="Close"></span>
                      </div>
                                
                                """)

    return render(request, 'login.html',{"next_url":next_url})


# Change password view
@login_required(login_url='/login/')
def change_password_view(request):
    form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password/change_password.html',{"form":form})

# Change password form component
@login_required(login_url='/login/')
def change_password_form(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse()
            response["HX-Redirect"]= '/login/'
            return response
        else:
            return render(request, 'change_password/change_password_form.html',{"form":form})