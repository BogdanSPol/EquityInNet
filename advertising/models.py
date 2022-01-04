from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CarouselAds(models.Model):
    image = models.ImageField(upload_to='advertising/carousel/db/images/')
    url = models.URLField(blank=True)
    chapter = models.CharField(max_length=30)
    title = models.CharField(max_length=28)
    status_choices = [
        ('ACTIVE', 'Active'),
        ('END', 'End'),
        ('NOT_AVAIL', 'N/A'),
    ]
    status = models.CharField(
        max_length=9,
        choices=status_choices,
        default='NOT_AVAIL',
    )
    date_to_go = models.DateTimeField()
    date = models.DateField()
    slug = models.SlugField(default='', null=False, db_index=True)

#    def save(self, *args, **kwargs):
#        self.slug = slugify(self.title)
#        super(CarouselAds, self).save(*args, **kwargs)

#    def get_url(self):
#        return reverse('detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} - {self.chapter} - {self.status}'
