from django.db import models


class Location(models.Model):
    created_by = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=300, default='Another Spyfell Session')
    created = models.DateTimeField('created', auto_now_add=True)
    current_location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=300)
    active_session = models.ForeignKey(Session, null=True, on_delete=models.SET_NULL)
    current_location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    is_spy = models.BooleanField(default=False)

    def __str__(self):
        return self.name