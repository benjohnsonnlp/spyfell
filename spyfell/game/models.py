from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=300, default='Another Spyfell Session')
    created = models.DateTimeField('created', auto_now_add=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=300)
    active_session = models.ForeignKey(Session)