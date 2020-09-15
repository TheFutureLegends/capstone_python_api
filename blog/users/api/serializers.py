from rest_framework import serializers
from blog.users.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
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
