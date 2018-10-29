# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db.models import Func, F
from app.models import *


class UDFMixin:
    """
    This mixin tests a queryset that depends on the User-defined function.
    """
    # NOTE: done as a mixin to force many, many tests.
    fixtures = ['sarahbooks']

    def test_udf(self):
        sarah = Author.objects.annotate(hello=Func(F('first_name'), function='HELLO')).filter(first_name='Sarah').first()
        self.assertEqual(sarah.hello, 'Hello, Sarah!')


class TestOne(UDFMixin, TestCase):
    pass


class TestTwo(UDFMixin, TestCase):
    pass


class TestThree(UDFMixin, TestCase):
    pass


class TestFour(UDFMixin, TestCase):
    pass


class TestFive(UDFMixin, TestCase):
    pass


class TestSix(UDFMixin, TestCase):
    pass


class TestSeven(UDFMixin, TestCase):
    pass


class TestEight(UDFMixin, TestCase):
    pass

