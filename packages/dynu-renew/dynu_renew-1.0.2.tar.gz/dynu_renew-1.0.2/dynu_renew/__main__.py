"""dynu_renew.__main__ file."""

from os import mkdir
from os.path import isdir, join
from shutil import copyfile

from dynu_renew import renew_domains_ip

if __name__ == '__main__':
    if not isdir('instance'):
        mkdir('instance')
        copyfile(join('configs', 'config.py'), join('instance', 'config.py'))
        raise Exception('Missing "config.py" file into "instance" folder. Was created.')  # pylint: disable=broad-exception-raised

    renew_domains_ip()
