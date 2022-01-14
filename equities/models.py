from django.db import models
from django.urls import reverse
from datetime import date
from django.utils.text import slugify
from common.models import Currency, SectorChoice


class EquityProject(models.Model):
    image = models.ImageField(upload_to='equities/db/images/',)
    title = models.CharField(max_length=25,)
    url = models.URLField(blank=False, )
    end_date = models.DateField(
        blank=False,
        help_text="Day to go + date now",
    )
    currency = models.ForeignKey(
        'common.Currency',
        to_field="currency_abbr",
        on_delete=models.DO_NOTHING,
        null=True,
    )
    invested = models.PositiveSmallIntegerField(blank=False,)
    round_money = models.PositiveSmallIntegerField(
        blank=False,
        help_text="Target or Max round",
    )

    pre_money_valuation = models.PositiveSmallIntegerField(blank=False,)
    min_investment_amount = models.PositiveSmallIntegerField(blank=False,)

    sector_choice = models.ForeignKey(
        'common.SectorChoice',
        to_field="sector_name",
        on_delete=models.DO_NOTHING,
        null=True,
        default='NONE',
        help_text="In classification of yahoo.finance",
    )

    date_last_modified = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
    add_date_time = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    slug = models.SlugField(
        default='',
        null=False,
        db_index=True,
        editable=False,
    )
    is_active = models.CharField(
        default='',
        null=False,
        db_index=True,
        editable=False,
        max_length=6,
    )
    score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        editable=True,
        default=0,
        db_index=True,
    )

    @property
    def status(self, *args, **kwargs):
        if date.today() > self.end_date:
            res = "ENDED"
        else:
            res = "ACTIVE"
        self.is_active = res
        self.slug = slugify(self.title)
        super(EquityProject, self).save(*args, **kwargs)
        return res

    @property
    def min_amount(self):
        if self.currency_id in ['GBP', 'EUR']:
            return f'{self.min_investment_amount:,} {self.currency.currency_sign}'
        else:
            return f'{self.currency.currency_sign} {self.min_investment_amount:,}'

    @property
    def pre_money_val(self):
        if self.currency_id in ['GBP', 'EUR']:
            return f'{self.pre_money_valuation:,} {self.currency.currency_sign}'
        else:
            return f'{self.currency.currency_sign} {self.pre_money_valuation:,}'

    @property
    def round_raised(self):
        if self.currency_id in ['GBP', 'EUR']:
            return f'{self.invested:,} {self.currency.currency_sign} of ' \
               f'{self.round_money:,} {self.currency.currency_sign}'
        else:
            return f'{self.currency.currency_sign} {self.invested:,} of ' \
                   f'{self.currency.currency_sign} {self.round_money:,}'

    @property
    def raised_percent(self):
        return f'{((self.invested *10000) // self.round_money) / 100}%'

    @property
    def days_to_go(self):
        return self.end_date - date.today()

    def get_url(self):
        return reverse('detail', args=[self.slug])

    def __str__(self):
        return self.title
