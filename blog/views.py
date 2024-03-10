from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Susan Fox',
        'title': 'Bogging with Django',
        'content': 'It takes a lot of work to set up a blog with Django.',
        'date_posted': 'March 3rd, 2024'
    },
    {
        'author': 'Susan Horton',
        'title': 'What It Is like to become a Fox',
        'content': 'Although I like being a Fox, I miss being a Horton.',
        'date_posted': 'March 3rd, 2024'
    }
]

def home(request):
    context = {
        'posts': posts    
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')


