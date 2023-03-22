from django.contrib import admin
from .models import Post
from import_export import resources
#cari python3 di env biar nda ada tandanya
from import_export.fields import Field
# Register your models here.


class PostResource(resources.ModelResource):
    #adjust field
    is_active= Field()
    created=Field()
    
    class Meta:
        model = Post
        field=('id','title','description','is_active','created')
        export_order=('id','description','is_active','title','created')
    
    # untuk mengganti format di excel
    
    def dehydrate_is_active(self,obj):
        if obj.is_active:
            return"yes"
        return"no"
    
    def dehydrate_created(self,obj):
        return obj.created.strftime("%d-%m-%Y %H:%M:%S")

admin.site.register(Post)