from django.db import models

# Create your models here.

class Social(models.Model):#Top Selling in Social Media Marketing
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Content(models.Model):#Top Selling in Content Marketing
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Email(models.Model):#Top Selling in Email Marketing
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Affiliate(models.Model):#Top Selling in Affiliate Marketing
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)

class Influencer(models.Model):#Top Selling in Influencer Marketing
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Video(models.Model):#Top Selling in Video Marketing
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Mobile(models.Model):#Top Selling in Mobile Marketing
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)