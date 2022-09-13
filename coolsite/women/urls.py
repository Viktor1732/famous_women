from django.conf.urls.static import static
from django.urls import path

from coolsite import settings
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
