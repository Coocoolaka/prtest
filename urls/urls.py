
urlpatterns = patterns('specifications.views',
                       # GET resources
                       (r'^$', 'index'),
                       (r'^/(?P<specification>\w+)/(?P<version>\w+)/resources$', 'resources'),
                       (r'^/resource/(?P<resource_id>\w+)$', 'resource'),
                       (r'^/(?P<resource_id>\w+)/elements$', 'elements'),


                       # POST resources
                       (r'^/specification$', 'specification'),
                       (r'^/resource$', 'resource'),
                       (r'^/element$', 'element')
                       )