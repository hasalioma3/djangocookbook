from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
# import get_object_or_404 from django
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from assets.models import Categories, Assets
from .forms import AssetForm, CategoryForm

# LIST OF ASSETS
class AssetsList(TemplateView):
    template_name = 'assets/assets_list.html'

    def get(self, request):
        assets = Assets.objects.all()
        return render(request, self.template_name, {'assets': assets})

# add new asset
class AddAsset(CreateView):
    model = Assets
    template_name = 'assets/add_asset.html'
    form_class = AssetForm
    success_url = '/'

# add new category
class AddCategory(CreateView):
    model = Categories
    template_name = 'assets/add_category.html'
    form_class = CategoryForm
    success_url = '/'

# edit asset details
class EditAsset(UpdateView):
    model = Assets
    template_name = 'assets/add_asset.html'
    form_class = AssetForm
    success_url = '/'

# asset details
class AssetDetail(DetailView):
    model = Assets
    template_name = 'assets/asset_detail.html'

# delete asset by url id
class DeleteAsset(DeleteView):
    
    model = Assets
    template_name = 'assets/delete_asset.html'
    success_url = '/'