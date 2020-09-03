from rest_framework import serializers
from posts.models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    # def create(self, validated_data):
    #     return Posts.objects.create(validated_data);

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title);
    #     instance.author = validated_data.get('author', instance.author);
    #     instance.email = validated_data.get('email', instance.email);
    #     instance.date = validated_data.get('date', instance.date);
    #     instance.save();
    #     return instance;

class PaginatedPostSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = PostsSerializer