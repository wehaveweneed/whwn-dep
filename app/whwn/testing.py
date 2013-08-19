from django_nose import NoseTestSuiteRunner

# subclass NoseTestSuiteRunner so we can pass in an
# extra argument to the nose-runner, "--exe", which
# makes nose run tests in .py files that are marked
# as executable (ls -l says "x").
# nose doesn't run these files by
# default because they may not be "import safe",
# meaning they could start doing their own thing
# just by importing them, which you might not want.

# when mounting a ntfs partition in linux, files might
# be marked as executable.  "--exe" allows people to
# run unit tests on their local machines when booted
# into linux with the github repository mounted on an
# ntfs partition.

# http://stackoverflow.com/questions/10330499/what-does-import-safe-mean-in-python
# http://stackoverflow.com/questions/1457104/nose-unable-to-find-tests-in-ubuntu

class WhwnTestSuiteRunner(NoseTestSuiteRunner):
    def run_suite(self, argv):
        return super(WhwnTestSuiteRunner, self).run_suite(
            argv #"nosetests"
            + ["--exe"]
            )
