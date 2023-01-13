from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey("users.User", related_name="ads", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    is_published = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="pictures")

    class Meta:
        verbose_name = "Объявления"
        verbose_name_plural = "Объявление"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорий"

    def __str__(self):
        return self.name
