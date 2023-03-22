from django.urls import path
from .views import PostsListView
#from posts import views

app_name="posts"

urlpatterns = [
    path('',PostsListView.as_view(),name='main'),
    #path('',views.PostListView,name='main'),
]