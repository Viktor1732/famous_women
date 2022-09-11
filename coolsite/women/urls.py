from django.conf.urls.static import static
from django.urls import path, re_path

from coolsite import settings
from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('cats/<int:catid>/', categories), #http://127.0.0.1:8000/cats/
    path('women/', index), #http://127.0.0.1:8000/women/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
