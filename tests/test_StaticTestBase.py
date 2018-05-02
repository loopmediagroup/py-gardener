import os
from lib.StaticTestBase import StaticTestBase


class TestStaticTestBase(StaticTestBase):
    ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
    TEST_DIR = os.path.join(ROOT_DIR, "tests")
    LIB_DIR = os.path.join(ROOT_DIR, "lib")
