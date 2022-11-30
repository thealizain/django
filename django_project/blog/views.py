
from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

# Create your views here.

#below is a jason data

posts = [
	{
		'author': 'Ali ',
		'title': 'post 1',
		'content':'content for blog post 1',
		'date_posted':'Feb 9, 2022'
	},
	{
		'author': 'Zain',
		'title': 'post 2',
		'content':'content for blog post 2',
		'date_posted':'Feb 10, 2022'
	}

	
]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html', context)

def about(request):
	return render(request,'blog/about.html', {'title':'About'})

 