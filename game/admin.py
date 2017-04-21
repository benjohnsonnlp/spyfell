from django.contrib import admin

from .models import Session, Player, Location

admin.site.register(Session)
admin.site.register(Player)
admin.site.register(Location)
