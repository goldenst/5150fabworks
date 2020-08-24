
from django.urls import path

app_name = 'carts'

from .views import (
    cart_home, cart_update, checkout_home
    )

urlpatterns = [
    path('', cart_home, name="home"),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update'),
]

