"""Todo URL configuration."""

from django.conf import settings, urls
from django.contrib import admin
from rest_framework import documentation, routers, schemas
from ttasks.views import TaskAPI, tasks

router = routers.DefaultRouter()
router.register('tasks', TaskAPI)

urlpatterns = [
    urls.url(r'^$', tasks, name='tasks'),
    urls.url(r'^api/v1/', urls.include(router.urls, namespace='v1')),
    urls.url(r'^rest_api/', urls.include('rest_framework.urls', namespace='rest_framework')),
    urls.url(r'^schema/', schemas.get_schema_view(title='Pastebin API')),
    urls.url(r'^docs/', documentation.include_docs_urls(title='Documentação', description='Live API')),
    urls.url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [urls.url(r'^__debug__/', urls.include(debug_toolbar.urls))]
