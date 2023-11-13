from setuptools import setup, Command, find_packages
import setuptools
import os

entry_points = {
    'console_scripts': [
        'r53collector=library.r53collector:main',
    ],
}

options = {
    'build_scripts': {
        'install_dir': '/usr/local/bin',  # or '/usr/bin'
    },
}


dist = setuptools.Distribution()
dist.entry_points = entry_points

dist.command_options['install'] = options

setup(
    name='r53collector',
    version='1.2.12',
    description='package description',
    packages=find_packages(),
    install_requires=['termcolor', 'boto3', 'openpyxl', 'ipaddress', 'dnspython'],
    keywords=['python', 'route53', 'excel', 'sso', 'aws', 'aws org', 'subdomains', 'dangling' , 'certificates'],
    author='name',
    author_email='your@email.com'
)

