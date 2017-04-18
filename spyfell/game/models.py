from django.db import models


class Location(models.Model):
    created_by = models.ForeignKey('Player')
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=300, default='Another Spyfell Session')
    created = models.DateTimeField('created', auto_now_add=True)
    current_location = models.ForeignKey(Location, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=300)
    active_session = models.ForeignKey(Session, null=True)
    current_location = models.ForeignKey(Location, null=True)

    def __str__(self):
        return self.name