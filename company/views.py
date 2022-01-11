from .models import Company
from django.shortcuts import render
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



def list_company(request):
    company = Company.objects.filter(user=request.user)

    context = {
        'companys': company
    }

    return render(request, 'index.html', context)

