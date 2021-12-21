from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import home

from clients import urls as clients_urls
from users import urls as users_urls
from products import urls as products_urls
from company import urls as company_urls

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/login/', 
        auth_views.LoginView.as_view(), 
        name='login'
    ),
     path('accounts/logout/', 
        auth_views.LogoutView.as_view(), 
        name='logout'
    ),
    path('user/', include(users_urls)),
    path('client/', include(clients_urls)),
    path('product/', include(products_urls)),
    path('company/', include(company_urls)),
    path('', home, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

