from rest_framework import serializers
from blog.showcases.models import Showcases


class ShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showcases
        fields = '__all__'

    # def create(self, validated_data):
    #     return PostComments.objects.create(validated_data);

    # def update(self, instance, validated_data):
    #     instance.content = validated_data.get('content', instance.content);
    #     instance.post_id = validated_data.get('post_id', instance.post_id);
    #     instance.parent_id = validated_data.get('parent_id', instance.parent_id);
    #     instance.created_at = validated_data.get('created_at', instance.created_at);
    #     instance.updated_at = validated_data.get('updated_at', instance.updated_at);
    #     instance.save();
    #     return instance;
