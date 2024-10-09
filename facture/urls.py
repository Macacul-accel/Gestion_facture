from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.user_action, name='user_action'),
    path('upload/', views.facture_upload, name='upload'),
    path('facture_list/', views.display_facture_view, name='list'),
    path('<int:pk>/', views.delete_facture, name='delete_facture'),
]
