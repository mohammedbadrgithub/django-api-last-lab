from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
from pages.models import Post


import json

from pages.serializer import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pages.models import Post




@csrf_exempt
def posts_api(request):
    if request.method =='GET':
        posts=Post.get_all_posts()
        serialized_posts=[]
        for post in posts:
            serialized_posts.append(PostSerializer(post).data)
        return JsonResponse(serialized_posts,safe=False)

    elif request.method=='POST':
        post_data=json.loads(request.body)
        post = Post.objects.create(**post_data)
        return JsonResponse(PostSerializer(post).data)


@csrf_exempt
def post_api(request,id):
    post=Post.get_post(id)
    if request.method=='GET':
        # get one object
        return JsonResponse(PostSerializer(post).data)
    elif request.method=='PUT':
        #update object
        update_data=json.loads(request.body)
        post.name=update_data['name']
        post.des=update_data['des']
        post.save()
        return JsonResponse(PostSerializer(post).data)
    elif request.method=='DELETE':
        # delete object by 
        post.delete()
        return JsonResponse({'delete':1})