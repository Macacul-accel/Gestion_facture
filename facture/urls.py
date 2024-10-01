from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import facture_image_view, success

urlpatterns = [
    path('upload/', facture_image_view, name='upload'),
    path('success/', success, name='sucess'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)