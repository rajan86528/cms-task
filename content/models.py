from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
class Content(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False, blank=False)
    body = models.TextField(max_length=300, null=False, blank=False)
    summary = models.TextField(null=True, blank=True)
    categories = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
       super().clean()
       if len(self.title) > 30:
          raise ValidationError("Title must not be more than 30 characters")
       if len(self.body) > 300:
          raise ValidationError("Body must not be more than 300 characters")
    def __str__(self):
      return self.title