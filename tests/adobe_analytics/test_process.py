import pytest

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

from dataeng_dataflow.adobe_analytics import process


def test_create_pcoll():
    pipeline = TestPipeline()
    pcoll = pipeline | 'test' >> process.create_pcoll([1, 2, 3])
    assert_that(pcoll, equal_to([1, 2, 3]))
    pipeline.run()
