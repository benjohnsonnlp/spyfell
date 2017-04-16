from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=300, default='Another Spyfell Session')
    created = models.DateTimeField('created')

    def __str__(self):
        return self.name
