import os
import pytest
from py_gardener.TestDocker import TestDocker


class TestTestDocker(TestDocker):

    DOCKER = ["lambda"]

    def test_in_docker(self):
        exists_original = os.path.exists
        os.path.exists = lambda path: True

        self.test_docker()

        # revert
        os.path.exists = exists_original

    def test_not_in_docker(self):
        exists_original = os.path.exists
        os.path.exists = lambda path: False

        with pytest.raises(AssertionError) as err:
            self.test_docker()
        assert err.value.args[0] == 'Please run in Docker using ". manage.sh"'

        # revert
        os.path.exists = exists_original
