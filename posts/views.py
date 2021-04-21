from .models import Profile, Post
from .forms import CreatePostForm
from django.contrib import messages
from django.views.generic import (
        ListView, 
        DetailView, 
        UpdateView, 
        DeleteView
    )
from django.shortcuts import (
        render, 
        redirect, 
        get_object_or_404, 
        HttpResponseRedirect,
        )

# Create your views here.

def index(request):

    context = {

        }

    return render(request, 'posts/index.html', context)


def profile(request):

    profile = Profile.objects.all()

    context = {
        'profile':profile
        }

    return render(request, 'posts/profile.html', context)

class PostList(ListView):
    model = Post
    template_name = 'posts/postlist.html'
    context_object_name = 'postlist'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/postdetail.html'
    context_object_name = 'postdetail'


def postcreate(request):
    context = []
    user = request.user
    
    form = CreatePostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Profile.objects.filter(user=user).first()
        obj.author = author
        obj.save()
        messages.success(request, "post created successfully...")
        return redirect('posts:index')
        form = CreatePostForm()
    
    context={
        'form':form,
        }        

    
    return render (request, 'posts/postcreate.html', context)