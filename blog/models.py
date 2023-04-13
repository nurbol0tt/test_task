from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(
        max_length=55,
    )

    def get_absolute_url(self):
        return reverse("categories")


class Article(models.Model):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/",
    )

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('article_detail', args=(str(self.id),))