from django.db import models
from django.utils import timezone
from django.utils.html import format_html
import uuid
from django.urls import reverse


# Create your models here.


class Tree(models.Model):
    creator = models.CharField(max_length=50)
    title = models.CharField(max_length=150, default='My Branches')
    published = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    #    unique_id = get_random_string(length=15)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=True, unique_for_date='published')

    def get_unique_id(self):
        return reverse('tree:tree_detail',
                       args=[self.title, str(self.unique_id).replace('-', '')])

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title


class Branch(models.Model):
    tree = models.ForeignKey(Tree,
                             on_delete=models.CASCADE,
                             related_name='branches')
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200)

    def full_url(self):
        return format_html(f'<a href="{self.url}" target="_blank">{self.url}</a>') if len(
            self.url) < 50 else format_html(f'<a href="{self.url}" target="_blank">{self.url[:30]}...</a>')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Branch {self.title} created for {self.tree} with {self.tree.unique_id} ID'
