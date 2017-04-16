from django.db import models


class Sessions(models.Model):
    name = models.CharField(max_length=300, default='Another Spyfell Session')
    created = models.DateTimeField('created')