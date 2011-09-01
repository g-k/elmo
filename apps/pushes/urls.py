from django.conf.urls.defaults import patterns

urlpatterns = patterns('pushes.views',
                       (r'^pushes/(?P<repo_name>.+)?$', 'pushlog'),
                       (r'^diff$', 'diff'),
                       (r'^api/network$', 'api.network'),
                       (r'^api/forks/(.+)/?$', 'api.forks'),
)
