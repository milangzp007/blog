from django.urls import include, path
from django.conf.urls import url,static
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from blog import settings
from django.contrib import admin
# from comments import views as CommentsViews
schema_view = get_swagger_view(title='Milan API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/$', schema_view),
    url(r'^api/', include('comments.urls'))
    # url(r'^api/blog/', CommentsViews.BlogViews)
    
]