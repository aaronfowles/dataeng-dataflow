import argparse
import logging

import apache_beam as beam


def create_pcoll(list_contents):
    return beam.Create(list_contents)


def run():
    pass


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--runner')

    args = arg_parser.parse_args()

    runner = args.runner

    logging.info('Using {runner} runner'.format(runner=runner))

    with beam.Pipeline('DirectRunner') as p:
        pcoll = p | 'Create' >> create_pcoll([1, 2, 3])
        pcoll | 'Write' >> beam.io.WriteToText('test_output_file')

    run()
