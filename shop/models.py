from django.db import models
import string
import random

from reviews.models import Review


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.title


def generate_review_code():
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if not Purchase.objects.filter(review_code=code).exists():
            break

    return code


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    genshin_uid = models.CharField(max_length=9, null=True)
    review_code = models.CharField(default=generate_review_code, unique=True, editable=False, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
