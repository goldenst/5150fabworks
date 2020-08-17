from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from django.contrib import admin
from django.urls import path

from carts.views import cart_home

from .views import landing, about, contact, login_page, register_page


urlpatterns = [
    path('', landing , name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('cart/', cart_home, name="cart"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('products/', include("products.urls", namespace="products")),
    path('search/', include("search.urls", namespace="search")),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)