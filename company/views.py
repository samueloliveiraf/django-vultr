from .models import Company
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


class CrieteViewCompany(CreateView):
    template_name = 'company/create_company.html'
    model = Company
    
    fields = [
        'name',
        'image'
    ]
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  
    
    
    success_url = reverse_lazy('home')


class UpadateViewCompany(UpdateView):
    model = Company
    
    fields = [
        'name',
        'image'
    ]
    
    template_name = 'company/create_company.html'
    
    
    success_url = reverse_lazy('home')
