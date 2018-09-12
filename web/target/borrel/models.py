from django.db import models
from django.conf import settings

class Borrel(models.Model):
    """Model for a single item"""

    date = models.DateTimeField("Borrel datum")

    def __str__(self):
        return self.date.__str__()

class Entry(models.Model):
    borrel = models.ForeignKey(Borrel, on_delete=models.CASCADE)
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    drink = models.TextField(blank=False, max_length=256)
    food = models.TextField(blank=False, max_length=256)

    class Meta:
        unique_together = ('borrel', 'person',)
