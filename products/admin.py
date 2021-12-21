from django.contrib import admin
from .models import Product, Sale


admin.site.register(
    [
        Product, 
        Sale
    ]
)
