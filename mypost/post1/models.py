from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
"""GENDER_CHOICES = (
    (GENDER_MALE, _("남")),
    (GENDER_FEMALE, _("여"))
)"""

class Post(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField(null=True)
    #ender = models.CharField(_("gender"), choices=GENDER_CHOICES, max_length=10, blank=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    slice_location = models.FloatField(null=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)

    class Meta:
        ordering=['-published_date']


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
"""
class PostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(published_date__lte=now)
    
    def search(self, query):
        return self.filter(name__icontains=query)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)
"""