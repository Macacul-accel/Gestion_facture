from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.facture_upload, name='upload'),
    path('facture_image/', views.display_facture_view, name='facture_image'),
    path('<int:pk>/', views.delete_facture, name='delete_facture'),
]
