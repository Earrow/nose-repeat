# coding=utf-8

from nose.plugins import Plugin


class Repeat(Plugin):
    name = 'repeat'
    score = 10000

    def __init__(self):
        super().__init__()

        self._repeat_times = None

    def options(self, parser, env):
        super().options(parser, env)

        parser.add_option("--repeat-times", action="store", default=1, dest="repeat_times", help="Tests repeat times.")

    def configure(self, options, conf):
        super().configure(options, conf)

        if options.html_file:
            self._repeat_times = int(options.repeat_times)

    def prepareTestLoader(self, loader):
        repeat_times = self._repeat_times
        has_repeated = False

        class RepeatLoader(loader.__class__):
            def loadTestsFromModule(self, *args, **kwargs):
                suite = super(RepeatLoader, self).loadTestsFromModule(*args, **kwargs)

                nonlocal has_repeated
                if not has_repeated:
                    tests = list(suite._get_tests())
                    suite._set_tests(tests * repeat_times)
                    has_repeated = True

                return suite

            def loadTestsFromName(self, *args, **kwargs):
                suite = super(RepeatLoader, self).loadTestsFromName(*args, **kwargs)

                nonlocal has_repeated
                if not has_repeated:
                    tests = list(suite._get_tests())
                    suite._set_tests(tests * repeat_times)
                    has_repeated = True

                return suite

        loader.__class__ = RepeatLoader

        return None
