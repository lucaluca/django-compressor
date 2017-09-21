from compressor.conf import settings
from compressor.filters import CompilerFilter


class UglifyJSFilter(CompilerFilter):
    command = "{binary} {args}".format(
        binary=settings.COMPRESS_UGLIFY_JS_BINARY,
        args=settings.COMPRESS_UGLIFY_JS_ARGUMENTS
    )

    def __init__(self, *args, **kwargs):
        super(UglifyFilter, self).__init__(*args, **kwargs)
        self.command
