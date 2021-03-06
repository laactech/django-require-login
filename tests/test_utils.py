import unittest

from django_require_login import utils


class IsViewFuncPublicTests(unittest.TestCase):
    def test_False_when_not_present(self):
        def function():
            pass

        is_public = utils.is_view_func_public(function)

        self.assertFalse(is_public)

    def test_False(self):
        def function():
            pass

        function.REQUIRE_LOGIN_IS_PUBLIC = False

        is_public = utils.is_view_func_public(function)

        self.assertFalse(is_public)

    def test_True(self):
        def function():
            pass

        function.REQUIRE_LOGIN_IS_PUBLIC = True

        is_public = utils.is_view_func_public(function)

        self.assertTrue(is_public)


class SetViewFuncPublicTests(unittest.TestCase):
    def test_sets_attr(self):
        def function():
            pass

        utils.set_view_func_public(function)

        self.assertTrue(function.REQUIRE_LOGIN_IS_PUBLIC)
