import argparse
import logging
import sys

import apache_beam as beam


def create_pcoll(list_contents):
    return beam.Create(list_contents)


def run(argv=None):
    logging.getLogger().setLevel(logging.INFO)

    pipeline_options = beam.pipeline.PipelineOptions()

    with beam.Pipeline(options=pipeline_options) as p:
        pcoll = p | 'Read' >> beam.io.ReadFromText('gs://dev-alf-analytics/raw/*.csv')
        pcoll | 'Write' >> beam.io.WriteToText('gs://dev-alf-analytics/processed/processed', file_name_suffix='.csv')


if __name__ == '__main__':
    run()
