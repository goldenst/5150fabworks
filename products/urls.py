
from django.urls import path

app_name = 'products'

from .views import (
    ProductListView,  
    ProductDetailSlugView,
    ProductDetailView
    )

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('<slug>', ProductDetailSlugView.as_view(), name='detail'),
    # path('<pk>', ProductDetailView.as_view()),
]

