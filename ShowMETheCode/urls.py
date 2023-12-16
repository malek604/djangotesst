from django.urls import path ,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^(?P<slug>[\u0600-\u06FF0-9-]+)/$', views.accessory_detail, name='accessory_detail'),
    path('myview/', views.my_view, name='my_view'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
