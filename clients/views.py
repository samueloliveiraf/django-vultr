from django.views.generic import (
    CreateView, 
    ListView,
    DeleteView, 
    UpdateView,
)
from django.urls import reverse_lazy
from .models import Client


class ListViewClient(ListView):
    template_name = 'client/list_clients.html'
    model = Client
    paginate_by = 4

    
    def get_queryset(self):
        queryset = super(ListViewClient, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CrieteViewClient(CreateView):
    template_name = 'client/create_client.html'
    model = Client
    
    fields = [
        'name',
        'phone',
        'email'
    ]
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  
    
    
    success_url = reverse_lazy('list_client')


class UpadateViewClient(UpdateView):
    model = Client
    
    fields = [
        'name',
        'phone',
        'email'
    ]
    
    template_name = 'client/update_client.html'
    
    
    success_url = reverse_lazy('list_client')
    
    
class DeleteViewClient(DeleteView):
    model = Client
    template_name = 'client/delete_client.html'
    
    success_url = reverse_lazy('list_client')

