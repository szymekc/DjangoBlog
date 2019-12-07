from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.conf import settings
from .forms import PostForm

def post_list(request):
	if request.method == "GET":
		posts = Post.objects.all()
		
		return render(request, 'blog/post_list.html', {'posts':posts})

	

def add_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		print(settings.AUTH_USER_MODEL)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
		else:
			print("IS NOT VALID")
	return render(request, 'blog/add_post.html', {'form':PostForm()})