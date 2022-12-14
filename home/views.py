from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dish, Comment
from .form import RegistrationForm
from .form_commets import CommentForm
from django.views.generic import ListView, DetailView


# Create your views here.
# def index(request):
#     return render(request, "pages/home.html")

# def blog(request):
#    return render(request, 'pages/blog.html')

def list(request):
    data = {'Dishs': Dish.objects.all().order_by('name')}
    return render(request, "pages/home.html", data)
    

class DishListView(ListView):
    queryset = Dish.objects.all().order_by('name')
    template_name = 'pages/home.html'
    context_object_name = 'Dishs'

def DishView(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, dish=dish)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(pk)

    return render(request, "pages/test.html", {"dish": dish, "form": form})


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
           
    return render(request, 'pages/register.html', {'form': form})

