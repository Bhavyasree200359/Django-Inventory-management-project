from django.contrib import admin
from django.urls import path
from . import views  # Adjust the import according to your app's name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.item_list, name='item_list'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
]
