 from django.db import models

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    #prepopulated_fields = {"slug": ("name",)}
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    #price = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.ImageField(max_length=50)
    image = models.ImageField(max_length=50)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    #lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)
