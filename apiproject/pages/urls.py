from django.urls import path
from pages.views import post_api, posts_api 
urlpatterns = [
    path('api',posts_api,name='api.posts'),
    path('api/<int:id>',post_api,name='api.post'),
    
]
