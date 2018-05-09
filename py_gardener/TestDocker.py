import os
from py_gardener.InternalTestBase import InternalTestBase


class TestDocker(InternalTestBase):

    def test_docker(self):
        if "lambda" in self.DOCKER:
            assert os.path.exists(os.path.join("/.dockerenv"))
