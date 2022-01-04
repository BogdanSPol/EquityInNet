from django.db import models
from django.utils.text import slugify


class IPOProject(models.Model):
    image = models.ImageField(upload_to='ipos/db/images/')
    title = models.CharField(max_length=100)
    listing_exchange = models.CharField(max_length=100)
    broker_name = models.CharField(max_length=100)
    sale_url = models.URLField(blank=True)
    min_price = models.PositiveSmallIntegerField()
    max_price = models.PositiveSmallIntegerField()
    pre_money_valuation = models.PositiveSmallIntegerField()
    min_investment_amount = models.PositiveSmallIntegerField()
    sector = models.CharField(max_length=20)
    industry = models.CharField(max_length=20)
    sale_date_time = models.DateTimeField()
    date = models.DateField()
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(IPOProject, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
