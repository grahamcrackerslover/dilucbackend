from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    is_positive = models.BooleanField(null=False, blank=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    code_used = models.CharField(max_length=6, null=False, blank=False)

    def __str__(self):
        return self.name
