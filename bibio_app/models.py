from distutils.command.upload import upload
from tokenize import blank_re
from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    # TODO
class Book(models.Model):
    status_chois = [
        ('avialble', 'availble'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5,
                                decimal_places=2,
                                null=True,
                                blank=True)
    retal_price_day = models.DecimalField(max_digits=5,
                                          decimal_places=2,
                                          null=True,
                                          blank=True)
    retal_peroid = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=5,
                                       decimal_places=2,
                                       null=True,
                                       blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,
                              choices=status_chois,
                              null=True,
                              blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
