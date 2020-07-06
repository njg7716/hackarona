from django.shortcuts import render

from django.views import View
from django.views.generic import ListView, DetailView

from scanner.models import ScanPhoto

# Create your views here.
class IndexView(ListView):
    queryset = ScanPhoto.objects.all()
    template_name = 'index.html'

class ResultsView(DetailView):
    model = ScanPhoto
    template_name = 'results.html'