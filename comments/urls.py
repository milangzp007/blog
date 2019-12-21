from django.urls import include, path
from django.conf.urls import url,static
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from blog import settings
from django.contrib import admin
from . import views

router = routers.DefaultRouter()
router.register(r'blog', views.BlogViews)
router.register(r'comment', views.CommentsViews)
router.register(r'custum_blog', views.CustumBlog,basename="custum_blog")

urlpatterns = [
    path('', include(router.urls)),
# Leave the existing urls defined here
]