from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    
    path('',views.home, name= 'home'),
    path('data-per-client/<str:client_id>/', views.data_per_client, name= 'data-per-client' ),
    path('data-per-product/<str:product>/', views.data_per_product, name= 'data-per-product'),
    #path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.update_product, name="update_product"),
    path('delete_prod/<str:pk>/', views.delete_prod, name="delete_prod"),
    path('add_note/<str:pk>/', views.add_note, name="add_note"),
    path('delete_note/<str:pk>/', views.delete_note, name="delete_note"),
    path('master', views.master, name="master"),
    path('update_master/<str:pk>/', views.updateMaster, name="update_master"),
    path('master_add/', views.addProduct, name="master_add"),
    path('add_product/', views.createProduct, name="add_product"),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product')

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 