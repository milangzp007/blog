from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models as Models
from . import serializer
from rest_framework.decorators import action
# Create your views here.

class BlogViews(viewsets.ModelViewSet):
    queryset = Models.Blog.objects.all()
    serializer_class = serializer.BlogSerializer

class CommentsViews(viewsets.ModelViewSet):
    queryset = Models.Comments.objects.all()
    serializer_class = serializer.CommentsSerializer

class CustumBlog(viewsets.GenericViewSet):
    serializer_class = serializer.BlogSerializer
    @action(detail=False,methods=['post'],serializer_class=serializer.GetBlogWithCommentSerializer)
    def get_blog_with_comment(self, request):
        data = request.data
        user = request.user
        blog_id = data['blog_id']
        blog = Models.Blog.objects.get(pk=blog_id)
        # comment = Models.Comments.objects.filter(blog_id=blog_id)
        # comment = blog.comments_set.all()
        blog_json = serializer.BlogWithCommentsSerializer(blog,many=False).data
        return Response(blog_json)