from django.urls import include, path
from django.views.generic import ListView, DetailView
from scoreboard.models import Post

urlpatterns = [ 
                path('', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="scoreboard/scoreboard.html")),
              ]