from django.urls import path
from .views import ( 
    ListViewProduct, 
    CrieteViewProduct,
    UpadateViewProduct,
    DeleteViewProduct, 
    sale_product,
    list_sales,
    search_product,
    product_lack
)

from .pdfview import GeneratePDF


urlpatterns = [ 
    path('list/', 
        ListViewProduct.as_view(),
        name='list_products'
    ),
    path('create/', 
        CrieteViewProduct.as_view(), 
        name='create_product'
    ),
    path('edit/<int:pk>/', 
        UpadateViewProduct.as_view(), 
        name='update_product'
    ),
    path('delete/<int:pk>/', 
        DeleteViewProduct.as_view(), 
        name='delete_product'
    ),
    path('sale/<int:id_product>/', 
        sale_product, 
        name='sale_product'
    ),
    path('list-sales/', 
        list_sales, 
        name='list_sales'
    ),
    path('pdf/<int:id_sale>/',
        GeneratePDF.as_view(), 
        name="pdf"
    ),
    path('seach/', 
        search_product, 
        name='search_product'
    ),
    path('product-lack/', 
        product_lack,
        name='product_lack'
    )
]