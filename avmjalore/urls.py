from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "AVMPOORVCHHATRA Admin"
admin.site.site_title = "Avmpoorvchhatra Admin Portal"
admin.site.index_title = "Welcome to AVMpoorvchhatrajalore portal"

urlpatterns = [
        path("", views.index, name='avmform'),
        path("avmform", views.avmform, name='avmform')
        
]
