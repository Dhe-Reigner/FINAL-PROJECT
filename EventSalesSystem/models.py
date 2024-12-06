from django.db import models

# Create your models here.

class Dashboard(models.Model):#Top Selling in Dashboard overall of all marketing models
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
class Social(models.Model):#Top Selling in Social Media Marketing
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Content(models.Model):#Top Selling in Content Marketing
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Email(models.Model):#Top Selling in Email Marketing
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Affiliate(models.Model):#Top Selling in Affiliate Marketing
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)

class Influencer(models.Model):#Top Selling in Influencer Marketing
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Video(models.Model):#Top Selling in Video Marketing
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class Mobile(models.Model):#Top Selling in Mobile Marketing
    preview = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    product = models.CharField('Product',max_length=100, default='', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
   
    def __str__(self):
        return str(self.product)
    
class RemoteWork(models.Model):
    when_posted =  models.CharField(max_length=100, default='', blank=True, null=True)
    job_title = models.CharField(max_length=200, default='', blank=True, null=True)
    work_schedule = models.CharField(max_length=200, default='', blank=True, null=True)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    requirements = models.CharField(max_length=200, default='', blank=True, null=True)
    payment_verification = models.CharField(max_length=200, default='', blank=True, null=True)
    budget = models.CharField(max_length=200, default='', blank='', null=True)
    location = models.CharField(max_length=200, default='', blank=True, null=True)
    proposal = models.CharField(max_length=200, default='', blank=True, null=True)
    
    def __str__(self):
        return self.job_title
    