from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile
from .forms import UserEditForm,ProfileEditForm
from posts.models import Post
from django.contrib.auth.models import User



class LogoutGetView(LogoutView):
    http_method_names = ['get', 'post', 'head', 'options']
    
    

def index(request):
    posts = Post.objects.all()
    return render(request,'users/index.html',{'posts':posts})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)   # so when the a new user register its profile also create automaticaly
            username = form.cleaned_data.get('username')
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render(request,'users/register.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES     # for the image field
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')  # or wherever you want after saving
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'users/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
    
@login_required   
def ProfileView(request):
    return render(request,'users/personal.html')

@login_required
def personalprofile(request):
    posts = Post.objects.filter(user=request.user)
    return render(request,'users/profile.html',{'posts':posts})


    
@login_required
def delete(request,id):
    Post.objects.get(pk=id).delete()
    return redirect('profile')





    


    
    

    
