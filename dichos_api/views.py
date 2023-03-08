from django.views.generic import TemplateView
from django.shortcuts import render

from django.views.generic import TemplateView


# def index(request):
#     return render(request, 'index.html')
class Home(TemplateView):
    template_name = "index.html"


class About(TemplateView):
    template_name = "about.html"
