import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repository', dest='repository')

    return parser
