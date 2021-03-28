from django.db import models
import django

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name