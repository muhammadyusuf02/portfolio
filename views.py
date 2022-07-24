from email.mime import image
from multiprocessing import context
from unicodedata import category
from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse


from about.forms import RegisterForm
from . models import About, Card, Karta, Rasm, Picture
# Create your views here.


def index(request):
    about = About.objects.all()
    print(about)
    card = Card.objects.all()[:3]
    rasm = Rasm.objects.all()[:2]
    karta = Karta.objects.all()[:5]
    picture = Picture.objects.all
    print(karta)
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = RegisterForm()

    return render(request, 'portfolio/index.html', context={'about': about, 'card': card, 'rasm': rasm, 'karta': karta, 'form': forms, 'picture': picture})

# def succeslogin(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('congragulation')
#     else:
#         form = RegisterForm()
#     return render(request, 'succeslogin.html',)


def about(request, slug):
    about = Card.objects.get(slug__iexact=slug)
    return render(request, 'portfolio/about.html', {'about': about})


# def category_detail(request, slug):
#     posts = About.objects.filter(category__slug=slug)
#     return render(request, 'portfolio/index.html', {'posts' : posts})
