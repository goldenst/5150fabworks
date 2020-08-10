from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404


from .models import Product
# Create your views here.
# -------------------------- LIST VIEW --------------------
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'


# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'products/list.html', context)

# ------------------------ DETAIL VIEW ------------------------------
class ProductDetailSlugView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        # except: Product.DoesNotExist:
        #     raise Http404("Not Found")
        # except: Product.MultipleObjectsReturned:
        #     qs = Product.objects.filter(slug=slug, active=True)
        #     instance = qs.first
        except: 
            raise Http404('Oops to many returned')
        return instance

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Product Not Found')
        return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)  

# def product_detail_view(request, pk=None, *args, **kwargs):
#     instance = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': instance
#     }
#     return render(request, 'products/detail.html', context)

# ------------------ FEATURED ---------------------------------------

class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/featured-detail.html'

    def get_queryset(self, *args, **kwargs):
         request = self.request
         return Product.objects.featured()