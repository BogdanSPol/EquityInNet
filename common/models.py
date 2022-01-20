from django.db import models


class Currency(models.Model):
    currency_name = models.CharField(max_length=50)
    currency_abbr = models.CharField(max_length=3, unique=True)
    currency_sign = models.CharField(max_length=10)

    def __str__(self):
        return self.currency_abbr


class SectorChoice(models.Model):
    sector_name = models.CharField(max_length=22, unique=True)
    sector_description = models.CharField(max_length=300)

    def __str__(self):
        return self.sector_name


class Country(models.Model):
    country_code = models.CharField(max_length=2, unique=True, null=True)
    country_name = models.CharField(max_length=32)
    country_flag = models.ImageField(upload_to='common/country_flags/',)

    def __str__(self):
        return self.country_code
