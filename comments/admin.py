from django.contrib import admin
from . import models as Models
# Register your models here.

admin.site.register(Models.Blog)
admin.site.register(Models.Comments)