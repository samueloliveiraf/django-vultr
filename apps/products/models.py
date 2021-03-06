from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    quantity = models.IntegerField(verbose_name='Quantidade', default=0 ,validators=[MinValueValidator(0)])
    image = models.ImageField(verbose_name='Imagem')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    product_min = models.IntegerField(verbose_name='Quantidade minima', default=0 ,validators=[MinValueValidator(0)])
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.name
    
    
    def total(self):
        total = self.quantity * self.price
        
        return total


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        
        return url
    

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=False,null=False)
    time = models.DateTimeField(auto_now=True)
    payment = models.CharField(max_length=100)
    quantity = models.IntegerField()
    name_client = models.CharField(max_length=150, verbose_name='Nome Cliente')


    class Meta:
        ordering = ['-id']


    def total_sale(self):
        total = self.product.price * self.quantity
        return total


    def __str__(self):
	    return '{} {} {} {} {}'.format(
            self.quantity, 
            self.product.quantity, 
            self.product.name, 
            self.time,
            self.payment,
        )
    
