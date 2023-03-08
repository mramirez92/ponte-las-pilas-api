from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Dicho


class DichoListView(ListView):
    template_name = "dichos/dicho_list.html"
    model = Dicho


class DichoDetailView(DetailView):
    template_name = "dichos/dicho_detail.html"
    model = Dicho

# Create your views here.
