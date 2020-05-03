from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^$', views.login, name='login'),
    # url(r'^sessions/', views.SessionList.as_view()),

    url(r'^player/submit$', views.save_player, name='save_player'),
    path('player/<int:player_id>/sessions', views.session_list, name='session_list'),
    path('player/<int:player_id>/sessions/<int:session_id>/', views.session, name='session_details'),
    path('player/<int:player_id>/sessions/<int:session_id>/submitLocation', views.save_location, name='save_location'),
    path('player/<int:player_id>/sessions/<int:session_id>/removeLocation', views.remove_location,
         name='remove_location'),
    path('player/<int:player_id>/sessions/create', views.create_session, name='create_session'),
    path('player/<int:player_id>/sessions/<int:session_id>/remove', views.remove_session, name='remove_session'),
    path('player/<int:player_id>/sessions/<int:session_id>/kick/<int:victim_id>', views.remove_player, name='remove_player'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
