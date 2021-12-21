from django.urls import path
from .views import CrieteViewCompany, UpadateViewCompany


urlpatterns = [
    path('create/', 
        CrieteViewCompany.as_view(), 
        name='create_company'
    ),
    path('edit/<int:pk>/',
        UpadateViewCompany.as_view(),
        name='update_company'
    )
]