from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

admin.site.site_header = "AVMPOORVCHHATRA Admin"
admin.site.site_title = "Avmpoorvchhatra Admin Portal"
admin.site.index_title = "Welcome to AVMpoorvchhatrajalore portal"

urlpatterns = [
    path("", views.index, name='avmform'),
    path("avmform", views.avmform, name='avmform')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
