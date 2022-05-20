from .views import AssetsList, AddAsset, AddCategory, EditAsset, DeleteAsset, AssetDetail
from django.urls import path

# namespace
app_name = 'assets'
urlpatterns = [
    path('', AssetsList.as_view(), name='assets_list'),
    path('add_asset/', AddAsset.as_view(), name='add_asset'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('edit_asset/<int:pk>/', EditAsset.as_view(), name='edit_asset'),
    path('delete_asset/<int:pk>/', DeleteAsset.as_view(), name='delete_asset'),
    path('asset_detail/<int:pk>/', AssetDetail.as_view(), name='asset_detail'),

]
