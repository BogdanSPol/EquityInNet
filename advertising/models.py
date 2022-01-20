from django.db import models


class CarouselAd(models.Model):
    image = models.ImageField(upload_to='advertising/carousel/db/images/')
    url = models.URLField(blank=True)
    chapter = models.CharField(max_length=35)
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

    def __str__(self):
        return f'{self.title} - {self.chapter} - {self.status}'
