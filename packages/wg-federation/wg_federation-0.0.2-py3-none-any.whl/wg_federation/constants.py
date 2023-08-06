"""
    Defines all constants for wg-federation
"""
import os

CHANGELOG_FILENAME = 'CHANGELOG.md'
VERSION_FILENAME = '__version__.txt'
__version__ = 'UNDEFINED'

pwd = os.path.dirname(os.path.realpath(__file__))


def read_version(filename: str):
    with open(filename, encoding='utf-8') as version_file:
        return version_file.readline().rstrip()


try:
    __version__ = read_version(os.path.join(pwd, '../../', CHANGELOG_FILENAME))
except FileNotFoundError:
    __version__ = read_version(os.path.join(pwd, VERSION_FILENAME))
