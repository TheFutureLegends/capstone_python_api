from rest_framework import serializers
from posts_comments.models import PostComments


class PostCommentsSerializer(serializers.ModelSerializer):
    # content = serializers.TextField() post_id = serializers.ForeignKey(Posts, related_name="post_id",
    # on_delete=models.CASCADE) parent_id = serializers.ForeignKey('self', related_name="comment_parent", null=True,
    # blank=True, on_delete=models.CASCADE) created_at = serializers.DateTimeField(auto_now_add=True) updated_at =
    # serializers.DateTimeField(auto_now_add=True)

    class Meta:
        model = PostComments
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
