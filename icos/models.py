from django.db import models
from django.utils.text import slugify


class ICOProject(models.Model):
    proj_logo = models.ImageField(upload_to='icos/db/images/')
    proj_name = models.CharField(max_length=100)
    proj_url = models.URLField(blank=True)
    tokensale_platform = models.CharField(max_length=100)
    tokensale_url = models.URLField(blank=True)
    token_type_choices = [
        ('COIN', 'Coin'),
        ('SECURITY', 'Security'),
        ('UTILITY', 'Utility'),
        ('NOT_AVAIL', 'N/A'),
    ]
    token_type = models.CharField(
        max_length=9,
        choices=token_type_choices,
        default='NOT_AVAIL',
    )
    tokensale_registration_deadline = models.DateTimeField()
    tokensale_start_date = models.DateTimeField()
    tokensale_end_date = models.DateTimeField()
    funding_methods = models.CharField(max_length=100)
    excluded_participants = models.CharField(max_length=200)
    min_investment_amount = models.PositiveSmallIntegerField()
    date = models.DateField()
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.proj_name)
        super(ICOProject, self).save(*args, **kwargs)

    def __str__(self):
        return self.proj_name
