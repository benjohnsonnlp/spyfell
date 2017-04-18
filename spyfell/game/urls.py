from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'game'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^$', views.login, name='login'),
    # url(r'^sessions/', views.SessionList.as_view()),
    url(r'^locations/submit', views.save_location, name='save_location'),
    url(r'^player/submit$', views.save_player, name='save_player'),
    url(r'^sessions/$', views.session_list, name='session_list'),
    url(r'^sessions/(?P<session_id>[0-9]+)/', views.session, name='session_details'),
    url(r'^sessions/create/$', views.create_session),
    url(r'^sessions/create/submit/$', views.save_session, name='session_create'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
