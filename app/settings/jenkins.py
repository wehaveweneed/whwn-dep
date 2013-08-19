
from settings.development import *

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': "http://elasticsearch.wehave-weneed.org:9200/",
        'INDEX_NAME': 'test',
    }
}
