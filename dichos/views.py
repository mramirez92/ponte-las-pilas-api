from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Dicho
# restfw
from rest_framework import generics
from .serializers import DichoSerializer


class DichoList(generics.ListCreateAPIView):
    queryset = Dicho.objects.all()
    serializer_class = DichoSerializer


class DichoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dicho.objects.all()
    serializer_class = DichoSerializer


#front views

# class DichoListView(ListView):
#     template_name = "dichos/dicho_list.html"
#     model = Dicho
#
#
# class DichoDetailView(DetailView):
#     template_name = "dichos/dicho_detail.html"
#     model = Dicho

# Create your views here.
