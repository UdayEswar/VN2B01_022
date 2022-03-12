from django.urls import path
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',name),
    path('vasanth',name1),
    path('suni',name2),
    path('vasanth/suni',name5),
    path('watsap',watsap),
    path('end/<city>',city),
    path('results',student),
    path('post',post),

 ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






