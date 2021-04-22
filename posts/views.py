from .models import Profile, Listing
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import  json
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
    model = Listing
    template_name = 'posts/postlist.html'
    context_object_name = 'postlist'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Listing
    template_name = 'posts/postdetail.html'
    context_object_name = 'postdetail'



@login_required
def postcreate(request):
    context = []
    user = request.user

    #You need to a way to handel GET & POST requests.
    #A GET requests is made when you visit this url so instantiate an empty form

    form = CreatePostForm()

    # This is what is processed during a POST request
    if request.is_ajax() and request.method == "POST":

        form = CreatePostForm(data = request.POST)
        if form.is_valid():

            #I have changed this so only authenicated users can view the page and submit the form.
            new_post = form.save(commit=False)
            new_post.author = user.profile
            new_post.save()

            messages.success(request, "post created successfully...")
            # return redirect('posts:index')
            # form = CreatePostForm()
		
            return HttpResponse(
                json.dumps({}),
                content_type="application/json"
                )

    #This is what is processed in a GET request  
    context={
        'form':form,
        }        
    return render (request, 'posts/postcreate.html', context)


'''
This has been taken from my GitHub
AJAX function to handle dropzone images
'''
@login_required
def dropzone_image(request):
	
	if request.method == "POST":
		
		user = request.user
		image = request.FILES.get('image')

        #Do something with the image here.....
		
		return HttpResponse({},content_type="application/json")

	return HttpResponse(
		json.dumps({"result": result, "message": message}),
		content_type="application/json"
		)