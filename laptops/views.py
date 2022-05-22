
from assets.models import Assets
from django.shortcuts import render
# import Paginator
from django.core.paginator import Paginator

# list assets that are laptops
def list_laptops(request):
    laptops = Assets.objects.filter(category_id=1).order_by('-id')
    # PAGINATE 
    paginator = Paginator(laptops, 10)
    page = request.GET.get('page')
    laptops1 = paginator.get_page(page)
    context = {
        'laptops': laptops1,}
    return render(request, 'laptops/list_laptops.html', context)



