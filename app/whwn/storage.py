from storages.backends.s3boto import S3BotoStorage
# from django.contrib.staticfiles.storage import StaticFilesStorage
from require.storage import OptimizedFilesMixin
from pipeline.storage import PipelineMixin
from django.contrib.staticfiles.storage import CachedFilesMixin
from itertools import chain

class PipelineRequiresStorage(OptimizedFilesMixin, PipelineMixin, S3BotoStorage):
    def post_process(self, paths, dry_run=False, verbosity=1, **options):
        requires = OptimizedFilesMixin.post_process(self, paths, **options)
        pipeline = PipelineMixin.post_process(self, paths, **options)
        return chain(requires, pipeline)
