from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class MenuItem(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=255, blank=True, unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
