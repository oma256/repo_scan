import argparse
import subprocess
import sys

if __name__ == '__main__':

    print('Downloading repository...')

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repository', dest='repository')

    args = parser.parse_args()
    repository = args.repository
    if not repository:
        parser.print_help()
        sys.exit(0)

    proc = subprocess.Popen(
        args=['git', 'clone', repository],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )

    print('Done')
