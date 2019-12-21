from rest_framework import serializers
from . import models as Models

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models.Blog
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(method_name="get_user")
    def get_user(self,obj):
        return obj.user.username
    class Meta:
        model = Models.Comments
        fields = "__all__"#("message","blog")
        extra_fields = ("username",)

class BlogWithCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(method_name="get_comments")
    username = serializers.SerializerMethodField(method_name="get_user")
    def get_user(self,obj):
        return obj.user.username
    def get_comments(self,obj):
        comments = obj.comments_set.all()
        return CommentsSerializer(comments,many=True).data
    class Meta:
        model = Models.Blog
        fields = ("title","content","created_date","username","comments")
    

class GetBlogWithCommentSerializer(serializers.Serializer):
    blog_id = serializers.IntegerField()
    class Meta:
        fields = ('blog_id')