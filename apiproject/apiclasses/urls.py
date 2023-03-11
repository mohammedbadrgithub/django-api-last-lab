from django.urls import path
from apiclasses.views import post_api_class , posts_api_class
urlpatterns = [
    path('class',posts_api_class,name='api.posts'),
    path('class/<int:id>',post_api_class,name='api.post'),
    
]
