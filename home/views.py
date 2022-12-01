from urllib import response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Dish
from .form import RegistrationForm
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
    template_name = 'pages/test.html'
    context_object_name = 'Dishs'

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin')
           
    return render(request, 'pages/register.html', {'form': form})

