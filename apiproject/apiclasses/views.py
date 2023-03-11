from django.shortcuts import render
from pages.models import Post
from pages.serializer import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
@api_view(['GET','POST'])
def posts_api_class(request):
    if request.method =='GET':
        posts=Post.get_all_posts()
        serialized_posts=[]
        PstSerializer = PostSerializer(posts,many=True )
        return Response(PstSerializer.data,status=status.HTTP_200_OK)

    elif request.method=='POST':
        post=PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
       
        return Response({'inserted':1},status=status.HTTP_200_OK)
@api_view(['GET','PUT','DELETE'])   
def post_api_class(request,id):
    
    post=Post.get_post(id)
    if request.method=='GET':
        # get one object
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        #update object
        post_serializer=PostSerializer(instance=post,data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response({'updated':1},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        # delete object by 
        post.delete()
        return Response({'deleted':1},status=status.HTTP_204_NO_CONTENT)