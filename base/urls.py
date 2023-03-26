from django.urls import path
from . import views



urlpatterns = [
    
    
    path('',views.home, name= 'home'),
    path('data-per-client/<str:client_id>/', views.data_per_client, name= 'data-per-client' ),
    path('data-per-product/<str:product_id>/', views.data_per_product, name= 'data-per-product'),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),
    path('add_note/<str:pk>/', views.addNote, name="add_note"),
    path('delete_note/<str:pk>/', views.delete_note, name="delete_note"),
    path('master', views.master, name="master"),
    path('update_master/<str:pk>/', views.updateMaster, name="update_master"),
    path('master_add', views.addProduct, name='master_add'),
    
    
] 
 