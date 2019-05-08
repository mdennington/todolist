from django.db import models
from django.urls import reverse

class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('id',)
        # set list and text as unique fields
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text



