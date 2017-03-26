import os

from setuptools import (
    find_packages,
    setup
)

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-scheduler',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    description='Task scheduler for Django',
    long_description=README,
    author='Tejas Jadhav',
    author_email='developer.tejas.jadhav@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
