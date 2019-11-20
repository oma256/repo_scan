import subprocess

from loguru import logger

from plugins.parser import get_repository_url


def run_git_clone_process():

    run_create_directory_command()
    subprocess.Popen(f"cd sendbox && git clone {get_repository_url()}",
                     shell=True,
                     stderr=subprocess.STDOUT,
                     stdout=subprocess.DEVNULL).communicate()
    logger.info("Done")


def run_create_directory_command():
    """ Create sendbox/ directory if not exist """

    subprocess.call(['./shell/create_directory.sh'])
