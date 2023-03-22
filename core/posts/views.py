from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,FormView
from .models import Post
from .forms import FormatForm
from .admin import PostResource
# Create your views here.

class PostsListView(ListView,FormView):
    model=Post
    template_name='posts/main.html'
    #form_class
    form_class=FormatForm
    
    def post(self,request,**kwargs):
        qs=self.get_queryset()
        dataset= PostResource().export(qs)
        
        format= request.POST.get('format')#get format yang di forms.py
        
        if format =='xls':
            ds = dataset.xls
        elif format == 'csv':
            ds = dataset.csv
        else:
            ds=dataset.json
        
        response = HttpResponse(ds,content_type=f"{format}")
        response['Content-Disposition']=f"attachment; filename=posts.{format}"
        return response