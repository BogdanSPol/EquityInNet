from django.db import models
from django.utils.text import slugify


class LoanProject(models.Model):
    image = models.ImageField(upload_to='equities/db/images/')
    title = models.CharField(max_length=100)
    loans_type = models.CharField(max_length=100)
    loans_broker = models.CharField(max_length=100)
    loans_url = models.URLField(blank=True)
    loans_amount = models.PositiveSmallIntegerField()
    loans_interest = models.DecimalField(max_digits=2, decimal_places=2)
    contract_period = models.CharField(max_length=20)
    days_to_go = models.PositiveSmallIntegerField()
    date = models.DateField()
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(LoanProject, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
