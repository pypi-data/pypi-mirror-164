import unittest
# from mtlibs import process_helper
from mtlibs.frpcProc import FrpcProc
# import asyncio
# from unittest import mock
from unittest.mock import patch
from ..github import gitUrlParse


class Test_Github(unittest.TestCase):
    def test_setupIfNeed(self):
        result  = gitUrlParse("https://github.com/codeh007/zappa_cms.git")
        print(result)
