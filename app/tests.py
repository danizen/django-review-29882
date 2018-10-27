# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


class TestFixturesAndUDF(TestCase):


    def test_fixture(self):
        sarah_counts = Author.objects.filter(first_name='Sarah').count()
        self.assertEqual(sarah_counts, 1)

    def test_udf(self):
        sarah = Author.objects.annotate(hello=Func(F('first_name'), function='HELLO')).filter(first_name='Sarah').first()
        self.assertEqual(sarah.hello, 'Hello, Sarah!')

