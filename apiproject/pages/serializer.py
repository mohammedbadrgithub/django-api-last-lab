from rest_framework import serializers
from pages.models import Post


class PostSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    des=serializers.CharField(max_length=200)
    no_of_likes=serializers.IntegerField(read_only=True)
    active=serializers.BooleanField(read_only=True)
    created_at=serializers.DateTimeField(read_only=True)
    updated_at=serializers.DateTimeField(read_only=True)
    
    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.des=validated_data.get('des',instance.des)
        instance.save()
        return instance