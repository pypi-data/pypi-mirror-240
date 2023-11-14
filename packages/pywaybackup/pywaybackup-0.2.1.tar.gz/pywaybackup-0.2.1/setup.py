
from setuptools import setup, find_packages
import pkg_resources

VERSION = '0.2.1'
DESCRIPTION = 'Download snapshots from the Wayback Machine'

def parse_requirements(filename):
    with open(filename, 'r') as f:
        requirements = [str(requirement) for requirement in pkg_resources.parse_requirements(f)]
    return requirements

setup(
    name='pywaybackup',
    version=VERSION,
    packages=find_packages(),
    install_requires=parse_requirements('./requirements.txt'),
    entry_points={
        'console_scripts': [
            'waybackup = waybackup.waybackup:main',
        ],
    },
    author='bitdruid',
    author_email='bitdruid@outlook.com',
    description=DESCRIPTION,
    license='MIT',
    keywords='wayback machine internet archive',
    url='https://github.com/bitdruid/waybackup',
)
