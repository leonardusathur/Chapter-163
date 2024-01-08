from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from . import models

def index(request):
     return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School
   
class SchoolUpdateView(UpdateView):
    fields = ("name","principal","location")
    model = models.School

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Base Views are Cools')