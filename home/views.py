from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dish, Comment
from .form import RegistrationForm
from .form_commets import CommentForm
from .form_dish import buy_dish_form
from django.views.generic import ListView, DetailView


# Create your views here.
# def index(request):
#     return render(request, "pages/home.html")

# def blog(request):
#    return render(request, 'pages/blog.html')


class DishListView(ListView):
    queryset = Dish.objects.all().order_by('price')
    template_name = 'pages/home.html'
    context_object_name = 'Dishs'

def DishView(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, dish=dish)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, "pages/dish.html", {"dish": dish, "form": form})


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
           
    return render(request, 'pages/register.html', {'form': form})


def dish(request, pk):
    dish = get_object_or_404(dish, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, dish=dish)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "pages/dish.html", {"dish": dish, "form": form})


# def buy_dish(request, dish_id):
#     current_user = request.user
#     product = Dish.objects.get(id=dish_id)
    
#     if request.method == 'POST':
#         for item in request.POST:
#             key = item
#             value = request.POST.get(key)
#             try:
#                 variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
#                 product_variations.append(variation)
#             except ObjectDoesNotExist:
#                 pass




