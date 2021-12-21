from django.urls import path
from .views import ( 
    CrieteViewClient, 
    ListViewClient,
    UpadateViewClient,
    DeleteViewClient
)


urlpatterns = [
    path('create/',
        CrieteViewClient.as_view(), 
        name='create_client'
    ),
    path('list/', 
        ListViewClient.as_view(), 
        name='list_client'
    ),
    path('edit/<int:pk>/', 
        UpadateViewClient.as_view(), 
        name='update_client'
    ),
    path('delete/<int:pk>/', 
        DeleteViewClient.as_view(), 
        name='delete_client'
    )
]