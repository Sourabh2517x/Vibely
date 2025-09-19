from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def PostCreationView(request):
    if request.method == 'POST':
        form = PostCreationForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            post = form.save(commit=False)   # commit=false means the data is not saved in database yet
            post.user = request.user  
            post.save()
            return redirect('index')  # change 'home' to any URL name you want to go to after posting
    else:
        form = PostCreationForm()

    return render(request, 'posts/post.html', {'form': form})

@login_required
def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'posts/user_posts.html', {
        'profile_user': user,
        'posts': posts
    })
     