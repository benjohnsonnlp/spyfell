from django.conf.urls import include, url
from django.contrib import admin

from foo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^$', views.index),
    url(r'^sessions/', views.SessionList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
