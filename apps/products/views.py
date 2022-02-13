from django.views.generic import (
    CreateView, 
    ListView,
    DeleteView, 
    UpdateView,
)
from django.urls import reverse_lazy

from apps.company.models import Company
from .models import Product, Sale
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
import datetime


class ListViewProduct(ListView):
    template_name = 'product/list_products.html'
    model = Product
    paginate_by = 4
    
    
    def get_queryset(self):
        queryset = super(ListViewProduct, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CrieteViewProduct(CreateView):
    template_name = 'product/create_products.html'
    model = Product
    
    fields = [
        'name',
        'quantity',
        'price',
        'image'
    ]
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  
    
    
    success_url = reverse_lazy('list_products')


class UpadateViewProduct(UpdateView):
    model = Product
    template_name = 'product/update_product.html'
    
    fields = [
        'name',
        'quantity',
        'price',
        'image'
    ]
    
    
    success_url = reverse_lazy('list_products')
    
    
class DeleteViewProduct(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    
    success_url = reverse_lazy('list_products')


@login_required(login_url='/accounts/login/')
def sale_product(request, id_product):
    template_name = 'product/sale_product.html'
    product = Product.objects.get(id=id_product, user=request.user)

    quantity = request.POST.get("quantity")
    payment = request.POST.get("payment")
    name_client = request.POST.get("name_client")

    qtd = int(quantity)

    if qtd <= product.quantity and product.quantity > 0:
        
        sales = Sale(
            quantity=quantity,
            product=product,
            payment=payment,
            name_client=name_client,
            user=request.user,
        )
        
        sales.save()

        product.quantity = product.quantity - int(quantity)
        product.save()

    else:
        message = 'Quantidade do produto é inválida'

        context = {
            'message': message
        }

        return render(request, 'product/erro_venda.html', context)

    context = {
        'sales': sales,
        'quantity': quantity,
        'product': product
    }

    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def list_sales(request):
    template_name = 'product/list_sales.html'
    
    startdata = request.GET.get('start_data')
    enddata = request.GET.get('end_data')

    if startdata != None and enddata != None:
        sales = Sale.objects.filter(
            user=request.user,
            time__range=(
            datetime.datetime.strptime(startdata,
            '%Y-%m-%d').date(),
            datetime.datetime.strptime(enddata,
            '%Y-%m-%d').date()),
        )
    else:
        sales = Sale.objects.filter(user=request.user)

    context = {
        'sales': sales,
    }

    return render(request, template_name, context)


@require_http_methods(['GET'])
def search_product(request):
    template_name = 'product/search_product.html'

    q = request.GET.get('q')

    if q:
        product = Product.objects.filter(name__icontains=q)

        context = {
            'product': product, 
            'query': q
        }

        return render(request, template_name, context)

    else:
        message = 'Busca vazia, informe o nome do produto'

        context = {
            'message': message
        }

    return render(request, 'product/erro_venda.html', context)


@login_required(login_url='/accounts/login/')
def product_lack(request):
    product_all = Product.objects.all()
    products_lack = product_all.filter(
        user=request.user,
        quantity__lte = F('product_min')
    )

    context = {
        'products_lack': products_lack
    }

    return render(request, 'product/lack.html', context)
