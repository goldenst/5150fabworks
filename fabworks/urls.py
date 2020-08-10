from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from django.contrib import admin
from django.urls import path


from .views import landing, about, contact, login_page, register_page


urlpatterns = [
    path('', landing , name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login_page),
    path('register/', register_page),
    path('products/', include("products.urls", namespace="products")),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<pk>', ProductFeaturedDetailView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products/<pk>', ProductDetailView.as_view()),
    # path('products/<slug>', ProductDetailSlugView.as_view()),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)